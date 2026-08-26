/**
 * Stress-case inputs are stored as compact generator specs (see runners/gen.py)
 * and only expanded inside the harness. Nothing in the UI should print the raw
 * spec at a user, so this renders a short human description instead.
 */

interface GeneratedSpec {
  __gen__: string;
  [key: string]: unknown;
}

function isSpec(value: unknown): value is GeneratedSpec {
  return typeof value === 'object' && value !== null && typeof (value as GeneratedSpec).__gen__ === 'string';
}

/** True when this value (or anything inside it) is generated at run time. */
export function isGenerated(value: unknown): boolean {
  if (isSpec(value)) {
    return true;
  }
  if (Array.isArray(value)) {
    return value.some(isGenerated);
  }
  return false;
}

function describeSpec(spec: GeneratedSpec): string {
  const n = spec.n as number | undefined;
  switch (spec.__gen__) {
    case 'ints':
      return `${n} random ints in [${spec.lo ?? 0}, ${spec.hi ?? 100}]`;
    case 'sorted':
      return `${n} sorted${spec.unique ? ' distinct' : ''} ints`;
    case 'perm':
      return `a shuffled permutation of ${n} values`;
    case 'string':
      return `a ${n}-character string over "${spec.alphabet ?? 'a-z'}"`;
    case 'words':
      return `${n} random words`;
    case 'grid':
      return `a ${spec.rows} x ${spec.cols} grid`;
    case 'pairs':
      return `${n} random pairs`;
    case 'edges':
      return `${n} ${spec.dag ? 'acyclic ' : ''}edges over ${spec.nodes} nodes`;
    case 'repeat':
      return `${JSON.stringify(spec.value)} repeated ${n} times`;
    case 'arange':
      return `${n} values from ${spec.start ?? 0} step ${spec.step ?? 1}`;
    case 'strrepeat':
      return `${JSON.stringify(spec.value)} repeated ${n} times`;
    case 'concat':
      return (spec.parts as unknown[]).map((part) => describe(part)).join(' + ');
    case 'shuffle':
      return `shuffled ${describe(spec.of)}`;
    case 'rotate':
      return `${describe(spec.of)} rotated by ${spec.by ?? 0}`;
    default:
      return `generated (${spec.__gen__})`;
  }
}

/** JSON for ordinary values, a readable summary for generated ones. */
export function describe(value: unknown, limit = 400): string {
  if (isSpec(value)) {
    return `⟨${describeSpec(value)}⟩`;
  }
  if (Array.isArray(value) && value.some(isGenerated)) {
    return `[${value.map((item) => describe(item, limit)).join(', ')}]`;
  }
  const text = JSON.stringify(value ?? null) ?? 'null';
  return text.length > limit ? `${text.slice(0, limit)}… (${text.length} chars)` : text;
}
