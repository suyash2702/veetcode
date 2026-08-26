export type Difficulty = 'Easy' | 'Medium' | 'Hard';

export type Language = 'python' | 'javascript';

/** How a returned value is compared against the expected value. */
export type CompareMode =
  | 'exact'          // deep equality
  | 'unordered'      // order of the top-level list is irrelevant
  | 'unordered2d'    // order of inner lists and of the outer list is irrelevant
  | 'approx'         // floats, 1e-5 tolerance
  | 'anyOf';         // expected holds a list of acceptable answers

/** Argument/return marshalling. Anything not listed is passed through as JSON. */
export type ValueType = 'json' | 'tree' | 'list' | 'list[]';

/**
 * Input shapes a plain array cannot express, built by the harness before the
 * solution is called: a list with a cycle, two lists sharing a tail, random
 * pointers, a list of bottom-linked columns.
 */
export type PrepareKind = 'graphNodes' | 'linkedCycle' | 'linkedIntersection' | 'randomList' | 'bottomList';

/** Serialisations that need the arguments, not just the returned value. */
export type ReturnType = ValueType | 'listpos' | 'randomlist' | 'bottomlist' | 'dllist' | 'nextlevels' | 'graph';

export interface TestCase {
  input: unknown[];
  output: unknown;
  /** Shown in the description panel and run by "Run Sample Tests". */
  sample?: boolean;
  explanation?: string;
}

/** LeetCode-style design problems: the solution defines a class, and a test
 * drives it with an operation list instead of a single call. */
export interface DesignSpec {
  className: string;
  /** Marshalling for the constructor arguments, e.g. a tree passed as an array. */
  constructorTypes?: ValueType[];
  /** Method names shown in the description panel; not used by the runner. */
  methods?: string[];
}

/**
 * Worked solution shown after the problem has been fought with — three failed
 * submits, or a solve. Code comes from the verified reference solution.
 */
export interface Editorial {
  /** Markdown walkthrough of the approach. */
  explanation: string;
  code: Partial<Record<Language, string>>;
  complexity?: string;
}

export interface Problem {
  id: number;
  slug: string;
  title: string;
  difficulty: Difficulty;
  tags: string[];
  /** Markdown, rendered in the description webview. */
  description: string;
  hints?: string[];
  functionName: string;
  params: string[];
  /** Per-position marshalling for arguments; defaults to 'json'. */
  paramTypes?: ValueType[];
  returnType?: ReturnType;
  /** Builds the argument list for shapes an array cannot express. */
  prepare?: PrepareKind;
  /**
   * For in-place problems: compare the mutated argument at this index
   * instead of the function's return value.
   */
  checkArg?: number;
  compare?: CompareMode;
  design?: DesignSpec;
  editorial?: Editorial;
  starter: Record<Language, string>;
  tests: TestCase[];
  complexity?: string;
}

export interface TestResult {
  index: number;
  passed: boolean;
  input: unknown[];
  expected: unknown;
  actual?: unknown;
  stdout?: string;
  error?: string;
  runtimeMs: number;
}

export interface RunSummary {
  problemSlug: string;
  language: Language;
  mode: 'sample' | 'submit';
  results: TestResult[];
  passed: number;
  total: number;
  totalMs: number;
  compileError?: string;
}
