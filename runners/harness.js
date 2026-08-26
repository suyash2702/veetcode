/**
 * VeetCode test harness (JavaScript).
 *
 * Usage: node harness.js <payload.json>
 *
 * The solution file is evaluated inside a vm context so that plain
 * `var twoSum = function (...) {}` top-level declarations — the shape
 * LeetCode-style starter code uses — are reachable without any exports.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { expand } = require('./gen.js');

const RESULT_PREFIX = '__VEETCODE_RESULT__';

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/** The graph node LeetCode uses for clone-graph. */
class Node {
  constructor(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

function buildTree(values) {
  if (!values || values.length === 0) return null;
  const root = new TreeNode(values[0]);
  const queue = [root];
  let i = 1;
  let head = 0;
  while (head < queue.length && i < values.length) {
    const node = queue[head++];
    if (i < values.length) {
      const v = values[i++];
      if (v !== null && v !== undefined) {
        node.left = new TreeNode(v);
        queue.push(node.left);
      }
    }
    if (i < values.length) {
      const v = values[i++];
      if (v !== null && v !== undefined) {
        node.right = new TreeNode(v);
        queue.push(node.right);
      }
    }
  }
  return root;
}

function dumpTree(root) {
  if (!root) return [];
  const out = [];
  const queue = [root];
  let head = 0;
  while (head < queue.length) {
    const node = queue[head++];
    if (node === null || node === undefined) {
      out.push(null);
      continue;
    }
    out.push(node.val);
    queue.push(node.left === undefined ? null : node.left);
    queue.push(node.right === undefined ? null : node.right);
  }
  while (out.length && out[out.length - 1] === null) out.pop();
  return out;
}

function buildList(values) {
  let head = null;
  for (let i = (values || []).length - 1; i >= 0; i--) head = new ListNode(values[i], head);
  return head;
}

function dumpList(head, limit = 10000) {
  const out = [];
  while (head && out.length < limit) {
    out.push(head.val);
    head = head.next;
  }
  return out;
}

// Some linked-list problems need a shape a plain array cannot express: a cycle,
// two lists sharing a tail, random pointers. A problem names one of these and
// the harness turns the raw test input into the arguments the solution sees.

function prepareLinkedCycle(raw) {
  const head = buildList(raw[0]);
  const pos = raw[1];
  if (pos !== null && pos !== undefined && pos >= 0 && head) {
    let node = head;
    for (let i = 0; i < pos; i++) node = node.next;
    let tail = head;
    while (tail.next) tail = tail.next;
    tail.next = node;
  }
  return [head];
}

function prepareLinkedIntersection(raw) {
  const tail = buildList(raw[2]);
  const withTail = (values) => {
    const head = buildList(values);
    if (!head) return tail;
    let node = head;
    while (node.next) node = node.next;
    node.next = tail;
    return head;
  };
  return [withTail(raw[0]), withTail(raw[1])];
}

function prepareRandomList(raw) {
  const pairs = raw[0];
  const nodes = pairs.map(([value]) => new ListNode(value));
  nodes.forEach((node, i) => {
    node.next = i + 1 < nodes.length ? nodes[i + 1] : null;
    const target = pairs[i][1];
    node.random = target === null || target === undefined ? null : nodes[target];
  });
  return [nodes.length ? nodes[0] : null];
}

function prepareBottomList(raw) {
  const heads = raw[0].map((values) => {
    let head = null;
    for (let i = values.length - 1; i >= 0; i--) {
      const node = new ListNode(values[i]);
      node.bottom = head;
      head = node;
    }
    return head;
  });
  heads.forEach((head, i) => {
    if (head) head.next = i + 1 < heads.length ? heads[i + 1] : null;
  });
  return [heads.length ? heads[0] : null];
}

function prepareGraphNodes(raw) {
  const adjacency = raw[0];
  const nodes = adjacency.map((_, i) => new Node(i + 1));
  adjacency.forEach((neighbours, i) => {
    nodes[i].neighbors = neighbours.map((j) => nodes[j - 1]);
  });
  return [nodes.length ? nodes[0] : null];
}

/** A cloned graph read back as an adjacency list, numbered from 1. */
function dumpGraph(node) {
  if (!node) return [];
  const seen = new Set();
  const byValue = new Map();
  const stack = [node];
  while (stack.length) {
    const current = stack.pop();
    if (seen.has(current)) continue;
    seen.add(current);
    byValue.set(current.val, current);
    for (const neighbour of current.neighbors) {
      if (!seen.has(neighbour)) stack.push(neighbour);
    }
  }
  return [...byValue.keys()].sort((a, b) => a - b).map((v) => byValue.get(v).neighbors.map((n) => n.val));
}

const PREPARES = {
  graphNodes: prepareGraphNodes,
  linkedCycle: prepareLinkedCycle,
  linkedIntersection: prepareLinkedIntersection,
  randomList: prepareRandomList,
  bottomList: prepareBottomList,
};

function dumpRandomList(head) {
  const nodes = [];
  for (let node = head; node; node = node.next) nodes.push(node);
  const index = new Map(nodes.map((node, i) => [node, i]));
  return nodes.map((node) => [node.val, node.random === null || node.random === undefined ? null : index.get(node.random)]);
}

function dumpBottomList(head, limit = 100000) {
  const out = [];
  for (let node = head; node && out.length < limit; node = node.bottom || null) out.push(node.val);
  return out;
}

/** A doubly linked list built out of tree nodes: walk `right` from the head. */
function dumpDll(head, limit = 100000) {
  const out = [];
  for (let node = head; node && out.length < limit; node = node.right || null) out.push(node.val);
  return out;
}

/** Levels read through the `next` pointers a solution wired up. */
function dumpNextLevels(root) {
  const out = [];
  let node = root;
  while (node) {
    const level = [];
    for (let cursor = node; cursor; cursor = cursor.next || null) level.push(cursor.val);
    out.push(level);
    let cursor = node;
    node = null;
    while (cursor && !node) {
      node = cursor.left || cursor.right || null;
      cursor = cursor.next || null;
    }
  }
  return out;
}

/** Index of `target` in the list at `head`, or -1. Bounded so a cycle terminates. */
function nodePosition(head, target, limit = 1000000) {
  if (!target) return -1;
  let node = head;
  for (let i = 0; i < limit; i++) {
    if (!node) return -1;
    if (node === target) return i;
    node = node.next;
  }
  return -1;
}

function marshalIn(value, kind) {
  if (kind === 'tree') return buildTree(value);
  if (kind === 'list') return buildList(value);
  if (kind === 'list[]') return (value || []).map(buildList);
  return value;
}

function marshalOut(value, kind, args) {
  if (kind === 'graph') return dumpGraph(value);
  if (kind === 'dllist') return dumpDll(value);
  if (kind === 'nextlevels') return dumpNextLevels(value);
  if (kind === 'listpos') return nodePosition(args ? args[0] : null, value);
  if (kind === 'randomlist') return dumpRandomList(value);
  if (kind === 'bottomlist') return dumpBottomList(value);
  if (kind === 'tree') return dumpTree(value);
  if (kind === 'list') return dumpList(value);
  if (kind === 'list[]') return (value || []).map((v) => dumpList(v));
  return value;
}

function toJson(value) {
  if (value === undefined) return null;
  if (value === null) return null;
  if (value instanceof TreeNode) return dumpTree(value);
  if (value instanceof ListNode) return dumpList(value);
  if (Array.isArray(value)) return value.map(toJson);
  if (value instanceof Set) return [...value].map(toJson);
  if (value instanceof Map) {
    const obj = {};
    for (const [k, v] of value) obj[String(k)] = toJson(v);
    return obj;
  }
  if (typeof value === 'number' && !Number.isFinite(value)) return String(value);
  if (typeof value === 'object') {
    const obj = {};
    for (const k of Object.keys(value)) obj[k] = toJson(value[k]);
    return obj;
  }
  return value;
}

function stable(value) {
  if (Array.isArray(value)) return '[' + value.map(stable).join(',') + ']';
  if (value && typeof value === 'object') {
    return '{' + Object.keys(value).sort().map((k) => JSON.stringify(k) + ':' + stable(value[k])).join(',') + '}';
  }
  return JSON.stringify(value === undefined ? null : value);
}

function deepEqual(a, b) {
  return stable(a) === stable(b);
}

function approxEqual(a, b, tol = 1e-5) {
  if (Array.isArray(a) && Array.isArray(b)) {
    return a.length === b.length && a.every((x, i) => approxEqual(x, b[i], tol));
  }
  if (typeof a === 'number' && typeof b === 'number') {
    return Math.abs(a - b) <= tol * Math.max(1, Math.abs(b));
  }
  return deepEqual(a, b);
}

function equal(actual, expected, mode) {
  if (mode === 'anyOf') return (expected || []).some((candidate) => deepEqual(actual, candidate));
  if (mode === 'approx') return approxEqual(actual, expected);
  if (mode === 'unordered') {
    if (!Array.isArray(actual) || !Array.isArray(expected)) return deepEqual(actual, expected);
    const norm = (rows) => rows.map(stable).sort();
    return deepEqual(norm(actual), norm(expected));
  }
  if (mode === 'unordered2d') {
    if (!Array.isArray(actual) || !Array.isArray(expected)) return deepEqual(actual, expected);
    const norm = (rows) => rows.map((row) => (Array.isArray(row) ? row.map(stable).sort().join('|') : stable(row))).sort();
    return deepEqual(norm(actual), norm(expected));
  }
  return deepEqual(actual, expected);
}

/**
 * LeetCode-style design problems: ops[0] is the constructor, the rest are
 * method calls, and the result list holds one entry per call (null for a
 * method that returns nothing).
 */
function runDesign(Ctor, ops, opArgs, ctorTypes) {
  const out = [];
  let instance = null;
  for (let i = 0; i < ops.length; i++) {
    let args = opArgs[i] || [];
    if (i === 0) {
      if (ctorTypes) args = args.map((a, j) => marshalIn(a, ctorTypes[j] || 'json'));
      instance = new Ctor(...args);
      out.push(null);
      continue;
    }
    const method = instance[ops[i]];
    if (typeof method !== 'function') {
      throw new Error(`no method "${ops[i]}" on ${Ctor.name || 'your class'}`);
    }
    const returned = method.apply(instance, args);
    out.push(returned === undefined ? null : toJson(returned));
  }
  return out;
}

function main() {
  const payload = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const paramTypes = payload.paramTypes || [];
  const returnType = payload.returnType || 'json';
  const checkArg = payload.checkArg === undefined ? null : payload.checkArg;
  const mode = payload.compare || 'exact';
  const design = payload.design || null;
  const prepare = PREPARES[payload.prepare] || null;
  const out = { results: [], compileError: null };

  let captured = '';
  const capture = (...args) =>
    (captured += args.map((a) => (typeof a === 'string' ? a : require('util').inspect(a, { depth: 4 }))).join(' ') + '\n');
  const sandboxConsole = { log: capture, error: capture, warn: capture, info: capture, debug: capture };

  const moduleStub = { exports: {} };
  const sandbox = {
    console: sandboxConsole,
    require,
    module: moduleStub,
    exports: moduleStub.exports,
    __filename: payload.solutionPath,
    __dirname: path.dirname(payload.solutionPath),
    TreeNode,
    ListNode,
    Node,
    setTimeout,
    clearTimeout,
    process,
    Buffer,
  };
  const context = vm.createContext(sandbox);

  let fn;
  try {
    const code = fs.readFileSync(payload.solutionPath, 'utf8');
    vm.runInContext(code, context, { filename: payload.solutionPath, timeout: payload.timeoutMs || 10000 });
    fn = resolve(context, moduleStub, design ? design.className : payload.functionName);
  } catch (err) {
    out.compileError = String((err && err.stack) || err);
    emit(out);
    return;
  }

  for (let index = 0; index < payload.tests.length; index++) {
    const test = payload.tests[index];
    let args;
    try {
      const raw = expand(test.input);
      args = prepare ? prepare(raw) : design ? raw : raw.map((v, i) => marshalIn(v, paramTypes[i] || 'json'));
    } catch (err) {
      out.results.push({ index, passed: false, runtimeMs: 0, error: 'bad test input: ' + err.message });
      continue;
    }
    const record = { index, passed: false, runtimeMs: 0, stdout: '' };
    captured = '';
    const started = process.hrtime.bigint();
    try {
      const returned = design ? runDesign(fn, args[0], args[1], design.constructorTypes) : fn.apply(null, args);
      const elapsed = Number(process.hrtime.bigint() - started) / 1e6;
      const produced = design
        ? toJson(returned)
        : checkArg !== null
          ? toJson(marshalOut(args[checkArg], paramTypes[checkArg] || 'json', args))
          : toJson(marshalOut(returned, returnType, args));
      record.actual = produced;
      record.passed = equal(produced, test.output, mode);
      record.runtimeMs = Math.round(elapsed * 1000) / 1000;
    } catch (err) {
      record.runtimeMs = Math.round(Number(process.hrtime.bigint() - started) / 1e3) / 1e3;
      record.error = String((err && err.stack) || err);
    }
    record.stdout = captured.slice(0, 4000);
    out.results.push(record);
  }

  emit(out);
}

/**
 * `var` and function declarations land on the context object, but `let`,
 * `const` and `class` only create lexical bindings — those have to be read
 * back by evaluating the identifier inside the same context.
 */
function lookup(context, name) {
  if (!/^[A-Za-z_$][A-Za-z0-9_$]*$/.test(name)) return undefined;
  if (typeof context[name] === 'function') return context[name];
  try {
    return vm.runInContext(`typeof ${name} === 'function' ? ${name} : undefined`, context);
  } catch (err) {
    return undefined;
  }
}

function resolve(context, moduleStub, name) {
  const candidates = [
    lookup(context, name),
    moduleStub.exports && moduleStub.exports[name],
    moduleStub.exports,
  ];
  for (const candidate of candidates) {
    if (typeof candidate === 'function') return candidate;
  }
  // A LeetCode-style `class Solution` is also accepted.
  const SolutionClass = lookup(context, 'Solution') || (moduleStub.exports && moduleStub.exports.Solution);
  if (typeof SolutionClass === 'function') {
    const instance = new SolutionClass();
    if (typeof instance[name] === 'function') return instance[name].bind(instance);
  }
  throw new Error(
    `no function named "${name}" found in your solution (declare it at the top level or export it)`
  );
}

function emit(payload) {
  process.stdout.write(RESULT_PREFIX + JSON.stringify(payload) + '\n');
}

main();
