/**
 * Deterministic expansion of generated test inputs — JavaScript port of
 * runners/gen.py. Both must produce identical output for the same spec;
 * expected outputs in problems/*.json are computed from the Python side.
 */
'use strict';

const MASK = 0xffffffff;
const LOWER = 'abcdefghijklmnopqrstuvwxyz';

class Rng {
  constructor(seed) {
    this.state = seed >>> 0;
  }

  next() {
    this.state = (this.state + 0x6d2b79f5) >>> 0;
    let t = this.state;
    t = Math.imul(t ^ (t >>> 15), t | 1) >>> 0;
    t = (t ^ (t + Math.imul(t ^ (t >>> 7), t | 61))) >>> 0;
    return (t ^ (t >>> 14)) >>> 0;
  }

  below(n) {
    return n > 0 ? this.next() % n : 0;
  }

  between(lo, hi) {
    return lo + this.below(hi - lo + 1);
  }

  pick(seq) {
    return seq[this.below(seq.length)];
  }
}

function shuffle(rng, items) {
  for (let i = items.length - 1; i > 0; i--) {
    const j = rng.below(i + 1);
    const tmp = items[i];
    items[i] = items[j];
    items[j] = tmp;
  }
  return items;
}

function oplogArg(spec, rng) {
  if (spec.int) return rng.between(spec.int[0], spec.int[1]);
  if (spec.choice) return rng.pick(spec.choice);
  if (spec.word) {
    const alphabet = spec.word.alphabet === undefined ? LOWER : spec.word.alphabet;
    const length = rng.between(spec.word.minLen === undefined ? 1 : spec.word.minLen,
                               spec.word.maxLen === undefined ? 6 : spec.word.maxLen);
    let out = '';
    for (let i = 0; i < length; i++) out += rng.pick(alphabet);
    return out;
  }
  throw new Error('unknown oplog argument: ' + JSON.stringify(spec));
}

const KINDS = {
  oplog(spec, rng) {
    const methods = spec.methods;
    const pool = [];
    methods.forEach((method, index) => {
      const weight = method.weight === undefined ? 1 : method.weight;
      for (let i = 0; i < weight; i++) pool.push(index);
    });
    let grower = methods.findIndex((m) => (m.delta || 0) > 0);
    if (grower < 0) grower = 0;

    const ops = [spec.cls];
    const args = [spec.ctor === undefined ? [] : spec.ctor];
    let size = 0;
    for (let i = 0; i < spec.n; i++) {
      let index = pool[rng.below(pool.length)];
      if (size < (methods[index].needs || 0)) index = grower;
      const method = methods[index];
      ops.push(method.name);
      args.push((method.args || []).map((arg) => oplogArg(arg, rng)));
      size = Math.max(0, size + (method.delta || 0));
    }
    return (spec.part === undefined ? 'ops' : spec.part) === 'ops' ? ops : args;
  },

  adj(spec, rng) {
    const out = [];
    for (let i = 0; i < spec.nodes; i++) out.push([]);
    for (let i = 0; i < (spec.n === undefined ? 0 : spec.n); i++) {
      const a = rng.below(spec.nodes);
      const b = rng.below(spec.nodes);
      out[a].push(b);
      if (!spec.directed) out[b].push(a);
    }
    return out;
  },

  zipsum(spec) {
    const parts = spec.parts.map(expand);
    const length = Math.min(...parts.map((p) => p.length));
    const out = new Array(length);
    for (let i = 0; i < length; i++) {
      let total = 0;
      for (const part of parts) total += part[i];
      out[i] = total;
    }
    return out;
  },

  duplicate(spec) {
    const times = spec.times === undefined ? 2 : spec.times;
    const out = [];
    for (const value of expand(spec.of)) {
      for (let i = 0; i < times; i++) out.push(value);
    }
    return out;
  },

  sortof(spec) {
    const values = expand(spec.of).slice();
    values.sort((a, b) => (spec.desc ? b - a : a - b));
    return values;
  },

  without(spec) {
    return expand(spec.of).filter((value) => value !== spec.value);
  },

  wedges(spec, rng) {
    const lo = spec.lo === undefined ? 0 : spec.lo;
    const hi = spec.hi === undefined ? 10000 : spec.hi;
    const out = [];
    if (spec.connected) {
      for (let i = 0; i < spec.nodes - 1; i++) out.push([i, i + 1, rng.between(lo, hi)]);
    }
    for (let i = 0; i < (spec.n === undefined ? 0 : spec.n); i++) {
      out.push([rng.below(spec.nodes), rng.below(spec.nodes), rng.between(lo, hi)]);
    }
    return out;
  },

  knows(spec, rng) {
    const n = spec.n;
    const density = spec.density === undefined ? 50 : spec.density;
    const matrix = [];
    for (let i = 0; i < n; i++) {
      const row = new Array(n);
      for (let j = 0; j < n; j++) row[j] = i === j ? 1 : rng.below(100) < density ? 1 : 0;
      matrix.push(row);
    }
    if (spec.celebrity !== undefined && spec.celebrity !== null) {
      for (let i = 0; i < n; i++) {
        matrix[spec.celebrity][i] = i === spec.celebrity ? 1 : 0;
        matrix[i][spec.celebrity] = 1;
      }
    }
    return matrix;
  },

  intervals(spec, rng) {
    const lo = spec.lo === undefined ? 0 : spec.lo;
    const hi = spec.hi === undefined ? 1000 : spec.hi;
    const maxLen = spec.maxLen === undefined ? 10 : spec.maxLen;
    const out = [];
    for (let i = 0; i < spec.n; i++) {
      const start = rng.between(lo, hi);
      out.push([start, start + rng.below(maxLen + 1)]);
    }
    return out;
  },

  disjoint(spec, rng) {
    const out = [];
    let cursor = spec.start === undefined ? 0 : spec.start;
    for (let i = 0; i < spec.n; i++) {
      cursor += rng.between(1, spec.gap === undefined ? 5 : spec.gap);
      const end = cursor + rng.below((spec.maxLen === undefined ? 5 : spec.maxLen) + 1);
      out.push([cursor, end]);
      cursor = end;
    }
    return out;
  },

  sortedgrid(spec, rng) {
    let value = spec.start === undefined ? 0 : spec.start;
    const out = [];
    for (let r = 0; r < spec.rows; r++) {
      const row = [];
      for (let c = 0; c < spec.cols; c++) {
        value += rng.between(1, spec.step === undefined ? 5 : spec.step);
        row.push(value);
      }
      out.push(row);
    }
    return out;
  },

  concat(spec) {
    const parts = spec.parts.map(expand);
    if (parts.length && parts.every((p) => typeof p === 'string')) return parts.join('');
    const out = [];
    for (const part of parts) {
      if (Array.isArray(part)) out.push(...part);
      else out.push(part);
    }
    return out;
  },

  strrepeat(spec) {
    return (spec.value === undefined ? 'a' : spec.value).repeat(spec.n);
  },

  shuffle(spec, rng) {
    const value = expand(spec.of);
    if (typeof value === 'string') return shuffle(rng, value.split('')).join('');
    return shuffle(rng, value.slice());
  },

  rotate(spec) {
    const value = expand(spec.of);
    const by = value.length ? ((spec.by === undefined ? 0 : spec.by) % value.length) : 0;
    return value.slice(by).concat(value.slice(0, by));
  },
  ints(spec, rng) {
    const lo = spec.lo === undefined ? 0 : spec.lo;
    const hi = spec.hi === undefined ? 100 : spec.hi;
    const out = new Array(spec.n);
    for (let i = 0; i < spec.n; i++) out[i] = rng.between(lo, hi);
    return out;
  },

  sorted(spec, rng) {
    let values = KINDS.ints(spec, rng);
    if (spec.unique) {
      values = [...new Set(values)].sort((a, b) => a - b);
      const step = Math.max(1, spec.step === undefined ? 1 : spec.step);
      while (values.length < spec.n) {
        const last = values.length ? values[values.length - 1] : spec.lo === undefined ? 0 : spec.lo;
        values.push(last + rng.between(1, step));
      }
    }
    values.sort((a, b) => (spec.desc ? b - a : a - b));
    return values;
  },

  perm(spec, rng) {
    const base = spec.base === undefined ? 0 : spec.base;
    const items = new Array(spec.n);
    for (let i = 0; i < spec.n; i++) items[i] = base + i;
    return shuffle(rng, items);
  },

  string(spec, rng) {
    const alphabet = spec.alphabet === undefined ? LOWER : spec.alphabet;
    let out = '';
    for (let i = 0; i < spec.n; i++) out += rng.pick(alphabet);
    return out;
  },

  grid(spec, rng) {
    const out = [];
    for (let r = 0; r < spec.rows; r++) {
      if (spec.alphabet !== undefined && spec.alphabet !== null) {
        let row = '';
        for (let c = 0; c < spec.cols; c++) row += rng.pick(spec.alphabet);
        out.push(spec.asString === false ? row.split('') : row);
      } else {
        const row = new Array(spec.cols);
        for (let c = 0; c < spec.cols; c++) {
          row[c] = rng.between(spec.lo === undefined ? 0 : spec.lo, spec.hi === undefined ? 1 : spec.hi);
        }
        out.push(row);
      }
    }
    return out;
  },

  pairs(spec, rng) {
    const lo = spec.lo === undefined ? 0 : spec.lo;
    const hi = spec.hi === undefined ? 100 : spec.hi;
    const out = new Array(spec.n);
    for (let i = 0; i < spec.n; i++) out[i] = [rng.between(lo, hi), rng.between(lo, hi)];
    return out;
  },

  repeat(spec) {
    return new Array(spec.n).fill(spec.value === undefined ? 0 : spec.value);
  },

  arange(spec) {
    const start = spec.start === undefined ? 0 : spec.start;
    const step = spec.step === undefined ? 1 : spec.step;
    const out = new Array(spec.n);
    for (let i = 0; i < spec.n; i++) out[i] = start + i * step;
    return out;
  },

  words(spec, rng) {
    const alphabet = spec.alphabet === undefined ? LOWER : spec.alphabet;
    const lo = spec.minLen === undefined ? 1 : spec.minLen;
    const hi = spec.maxLen === undefined ? 8 : spec.maxLen;
    const out = [];
    for (let i = 0; i < spec.n; i++) {
      const len = rng.between(lo, hi);
      let word = '';
      for (let c = 0; c < len; c++) word += rng.pick(alphabet);
      out.push(word);
    }
    return out;
  },

  edges(spec, rng) {
    const out = [];
    for (let i = 0; i < spec.n; i++) {
      let a = rng.below(spec.nodes);
      let b = rng.below(spec.nodes);
      if (spec.dag && a === b) continue;
      if (spec.dag && a < b) {
        const tmp = a;
        a = b;
        b = tmp;
      }
      out.push([a, b]);
    }
    return out;
  },
};

function expand(value) {
  if (Array.isArray(value)) return value.map(expand);
  if (value && typeof value === 'object') {
    const kind = value.__gen__;
    if (kind === undefined) {
      const out = {};
      for (const key of Object.keys(value)) out[key] = expand(value[key]);
      return out;
    }
    if (!KINDS[kind]) throw new Error('unknown generator kind: ' + kind);
    return KINDS[kind](value, new Rng(value.seed === undefined ? 1 : value.seed));
  }
  return value;
}

module.exports = { expand, Rng };
