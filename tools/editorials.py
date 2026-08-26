"""Editorial text, one entry per problem slug.

Only the prose lives here — the code shown alongside it is pulled from the
verified reference solution in tools/reference/, so an editorial can never
drift from a solution the judge actually accepts.

Editorials are locked in the UI until three submits have failed (or the
problem is solved), so write them as the explanation you would want *after*
trying, not as a hint.
"""

EDITORIALS = {}

EDITORIALS.update({
    "two-sum": """
The brute force checks every pair in `O(n^2)`. The trick is to stop thinking about pairs and think
about *complements*: while standing on `nums[i]`, the only value that helps is `target - nums[i]`.

Walk the array once, keeping a hash map from value to the index where you saw it. At each element,
look up the complement — if it is already in the map, you have your answer; otherwise record the
current value and move on. One pass, `O(n)` time and `O(n)` space.

Storing the value *after* the lookup is what stops an element from pairing with itself.
""",
    "valid-parentheses": """
A closing bracket must match the most recently opened one that is still open — that "most recent"
is the definition of a stack.

Push every opening bracket. On a closing bracket, pop: if the stack is empty or the popped bracket
is the wrong type, the string is invalid. At the end the stack must be empty, otherwise something
was opened and never closed.

`O(n)` time, `O(n)` space. Counting brackets instead of stacking them fails on `([)]`, which has
the right counts in the wrong order.
""",
    "best-time-to-buy-and-sell-stock": """
You only ever sell after you buy, so at each day the best possible profit is today's price minus
the cheapest price seen *so far*.

Sweep left to right keeping two numbers: the minimum price seen and the best profit seen. Both
update in constant time, so the whole thing is `O(n)` time and `O(1)` space.

This is Kadane's algorithm in disguise — run it on the array of day-to-day differences and you get
the same answer.
""",
    "contains-duplicate": """
Sorting first would make duplicates adjacent and costs `O(n log n)`. A hash set does better: walk
the array, and the first value that is already in the set is a duplicate.

`O(n)` time, `O(n)` space. In Python the whole thing collapses to comparing `len(set(nums))` with
`len(nums)`, which is the same algorithm with the loop hidden.
""",
    "valid-anagram": """
Two strings are anagrams exactly when their character counts match, so build a count map for one
string and tear it down with the other.

Compare lengths first — different lengths can never be anagrams and the check is free. Then count
`s`, subtract `t`, and check that nothing is left over. `O(n)` time, `O(1)` space for a fixed
alphabet.

Sorting both strings also works but costs `O(n log n)` for no benefit here.
""",
    "binary-search": """
Keep a window `[lo, hi]` that is the only place the target could still be. Compare with the middle
element: if it is smaller, the answer is to the right, so move `lo`; if larger, move `hi`.

Every comparison halves the window, so it finishes in `O(log n)` with `O(1)` space.

Two details bite people: use `lo + (hi - lo) // 2` in languages where `lo + hi` can overflow, and
be consistent about whether `hi` is inclusive — mixing the two conventions is how off-by-one
infinite loops happen.
""",
    "maximum-subarray": """
Kadane's algorithm. At each index ask one question: is it better to extend the previous subarray or
to start fresh here? The answer is `max(nums[i], best_ending_here + nums[i])`.

Track that running value plus the best seen anywhere, and the answer falls out in `O(n)` time and
`O(1)` space.

Starting `best` at negative infinity (not zero) is what makes all-negative arrays work — the answer
is then the largest single element.
""",
    "climbing-stairs": """
To reach step `n` you either came from `n - 1` with a single step or from `n - 2` with a double, so
`ways(n) = ways(n - 1) + ways(n - 2)` — the Fibonacci sequence with different starting values.

Recursion without memoisation recomputes the same steps exponentially. Iterating upwards with two
rolling variables is `O(n)` time and `O(1)` space.
""",
    "move-zeroes": """
Keep a write pointer for the next slot that should hold a non-zero value. Scan with a read pointer;
every time you find a non-zero, write it at the write pointer and advance it.

When the scan finishes, everything from the write pointer onwards is filled with zeroes. Relative
order of the non-zero values is preserved because they are copied in the order they were met.

`O(n)` time, `O(1)` space, and each element moves at most once.
""",
    "merge-sorted-array": """
Merging front to back would overwrite values in `nums1` that have not been read yet. Merging from
the **back** avoids that entirely: the tail of `nums1` is the free space.

Walk three pointers backwards — the end of the real data in `nums1`, the end of `nums2`, and the
end of the whole array — writing the larger of the two candidates each time.

When `nums2` runs out you are done; whatever is left in `nums1` is already in place. `O(m + n)`
time, `O(1)` space.
""",
    "reverse-linked-list": """
Walk the list once, flipping each `next` pointer to point at the node you just came from. You need
three references: the previous node, the current node, and the next node saved *before* you
overwrite the pointer.

When the current pointer falls off the end, the previous pointer is the new head. `O(n)` time,
`O(1)` space.

The recursive version reads nicely but costs `O(n)` stack, which matters on long lists.
""",
    "merge-two-sorted-lists": """
Standard merge: repeatedly take the smaller head and splice it into the result. Use a dummy head
node so the first element needs no special case, and keep a tail pointer to append in `O(1)`.

When one list runs out, attach the rest of the other in a single step — it is already sorted.

`O(m + n)` time and `O(1)` extra space, because the existing nodes are relinked rather than copied.
""",
    "invert-binary-tree": """
Inverting a tree means swapping the children of every node. Do it recursively: swap the two
children of the current node, then invert both subtrees.

`O(n)` time, `O(h)` stack. An iterative version with an explicit queue does the same work and is
worth reaching for if the tree can be deep enough to overflow the call stack.
""",
    "maximum-depth-of-binary-tree": """
The depth of a node is one more than the deeper of its two subtrees, and an empty tree has depth
zero. That sentence is the whole algorithm.

`O(n)` time, `O(h)` stack. A level-order traversal counting levels gives the same answer iteratively
and uses `O(width)` memory instead — the better choice for a very deep tree.
""",
    "majority-element": """
Boyer-Moore voting. Keep a candidate and a counter: matching values increase the counter,
different values decrease it, and a counter at zero adopts the current value as the new candidate.

An element that appears more than `n / 2` times cannot be cancelled out by everything else
combined, so it survives as the candidate. `O(n)` time, `O(1)` space.

Without the guarantee that a majority exists, a second pass to verify the candidate is required.
""",
    "group-anagrams": """
Anagrams need a canonical form that all members of a group share. Sorting the letters of a word
gives one (`"eat"` and `"tea"` both become `"aet"`), and so does a 26-slot letter-count tuple.

Bucket the words in a hash map keyed by that form. Sorting each word costs `O(k log k)`, giving
`O(n k log k)` overall; the count-tuple key drops it to `O(n k)`.
""",
    "longest-substring-without-repeating-characters": """
Slide a window that is always free of repeats. Extend it to the right one character at a time; when
the new character is already inside the window, move the left edge past its previous occurrence.

Storing the last index of each character lets the left edge jump straight there instead of crawling.
Each character is visited a constant number of times, so it is `O(n)` time and `O(alphabet)` space.

Moving the left edge only forwards — never backwards — is the detail that keeps it linear.
""",
    "product-of-array-except-self": """
Division would be easy and is disallowed (and breaks on zeroes anyway). Instead notice that the
answer at `i` is the product of everything to its left times the product of everything to its right.

One left-to-right pass fills the output with prefix products; one right-to-left pass multiplies in
the suffix products using a single running variable. `O(n)` time, and `O(1)` extra space if the
output array does not count.
""",
    "top-k-frequent-elements": """
Count occurrences in a hash map, then pick the `k` largest counts. Sorting the counts is
`O(n log n)`; a heap of size `k` is `O(n log k)`.

Bucket sort beats both: counts are bounded by `n`, so index an array by count, drop each value into
its bucket, and read buckets from the top until `k` values are collected — `O(n)` overall.
""",
    "coin-change": """
Unbounded knapsack. Let `best[amount]` be the fewest coins that make that amount; it is one more
than the best over `best[amount - coin]` for every coin that fits.

Fill the table upwards from `0` so every smaller amount is already solved, and use infinity for
amounts that cannot be made. `O(amount * coins)` time, `O(amount)` space.

Greedily taking the largest coin is wrong for arbitrary denominations — `[1, 3, 4]` for `6` is the
classic counterexample.
""",
    "number-of-islands": """
Every unvisited land cell starts a new island; flood filling from it removes the whole island from
consideration. Count how many times you have to start.

Sinking visited land by overwriting it with water avoids a separate visited set. Each cell is
touched a constant number of times, so it is `O(m * n)`.

Use an explicit stack or queue rather than recursion here: one island can cover the entire grid,
which is far more frames than most call stacks allow.
""",
    "course-schedule": """
The courses form a directed graph and the question is whether it has a cycle.

Kahn's algorithm answers it by construction: repeatedly remove a course with no remaining
prerequisites and decrement its dependents. If every course comes off the queue, a valid order
exists; anything left over is stuck in a cycle.

`O(V + E)` time and space. A DFS tracking nodes on the current recursion stack works equally well.
""",
    "3sum": """
Sort the array, then fix the first element and solve two-sum on the rest with two pointers moving
inwards: too small means advance the left pointer, too large means retreat the right one.

Sorting is what makes both the two-pointer sweep and duplicate skipping possible — skip equal
neighbours at every level and the output needs no de-duplication pass.

`O(n^2)` time and `O(1)` extra space beyond the sort.
""",
    "search-in-rotated-sorted-array": """
A rotated sorted array always has one half that is still sorted, and you can tell which by comparing
the middle element with the left end.

Check whether the target lies inside that sorted half: if it does, search there; if not, search the
other half. Each step halves the range, so it stays `O(log n)`.

Finding the rotation point first and then binary searching the right piece is the same idea written
as two passes.
""",
    "validate-binary-search-tree": """
Checking only that each node sits between its two children is not enough — a value can be legal
locally and still violate an ancestor's bound.

Carry a `(low, high)` interval down the recursion: going left tightens the upper bound to the
node's value, going right tightens the lower bound. A node outside its interval fails immediately.

`O(n)` time, `O(h)` stack. Equivalently, an inorder traversal of a BST is strictly increasing, so
comparing each value with the previous one works too.
""",
    "binary-tree-level-order-traversal": """
Breadth-first search, with the level boundary made explicit: before draining the queue, record how
many nodes are in it — that count is exactly the current level.

Process that many nodes, collecting values and enqueuing children, then start the next level.
`O(n)` time and `O(width)` space.
""",
    "house-robber": """
At each house there are two choices: rob it and add the best total from two houses back, or skip it
and keep the best total from the previous house.

That is `best[i] = max(best[i - 1], best[i - 2] + nums[i])`, and only the last two values are ever
needed — two rolling variables give `O(n)` time and `O(1)` space.
""",
    "longest-consecutive-sequence": """
Sorting solves it in `O(n log n)`, but a hash set gets it to `O(n)`.

Put every value in a set, then only start counting from values that begin a run — a value `x` where
`x - 1` is absent. From each start, walk upwards while the next value exists.

Every value is walked at most once across all runs, which is why the nested loop is still linear
overall.
""",
    "word-break": """
Let `ok[i]` mean "the first `i` characters can be segmented". It is true when some `j < i` has
`ok[j]` true and `s[j:i]` in the dictionary.

Fill the table left to right; the answer is `ok[n]`. With the dictionary in a hash set, this is
`O(n^2)` substring checks, or `O(n * maxWordLength)` if you only try lengths that exist.

Plain recursion without memoisation blows up exponentially on inputs like `"aaaa...b"`, which is
exactly what the stress cases here look like.
""",
    "spiral-matrix": """
Track four boundaries — top, bottom, left, right — and peel one edge at a time, shrinking the
boundary you just consumed.

The two guards that matter come after the first two edges: before walking the bottom row check that
`top <= bottom`, and before walking the left column check that `left <= right`. Without them a
single leftover row or column gets emitted twice.

`O(m * n)` time, `O(1)` extra space.
""",
    "rotate-image": """
Rotating by 90 degrees clockwise is a transpose followed by reversing each row — two in-place passes
with no extra matrix.

The transpose swaps `matrix[i][j]` with `matrix[j][i]` for `j > i` only; looping over all pairs
swaps everything twice and leaves the matrix unchanged.

`O(n^2)` time, `O(1)` space. Rotating four cells at a time in rings is equivalent and slightly
fiddlier to index.
""",
    "kth-largest-element-in-an-array": """
Sorting is `O(n log n)` and perfectly acceptable. A min-heap of size `k` improves it to
`O(n log k)`: push each value, and pop whenever the heap grows past `k`, so the root ends up as the
`k`-th largest.

Quickselect gets to `O(n)` on average by partitioning like quicksort but recursing into only the
side that contains the answer. Its worst case is `O(n^2)`, which a randomised pivot makes
vanishingly unlikely.
""",
    "unique-paths": """
Each cell can only be entered from above or from the left, so `paths[r][c] = paths[r-1][c] +
paths[r][c-1]`, with the first row and column all ones.

Filling row by row needs only the previous row, so one array of length `n` suffices — `O(m * n)`
time, `O(n)` space.

There is also a closed form: the answer is `C(m + n - 2, m - 1)`, since every path is a choice of
which moves are downward.
""",
    "longest-palindromic-substring": """
Every palindrome has a centre, and there are `2n - 1` of them — `n` characters and `n - 1` gaps.
Expand outwards from each centre while the characters match and keep the longest result.

`O(n^2)` time, `O(1)` space, and far easier to get right than the `O(n^2)` DP table.

Manacher's algorithm reaches `O(n)` by reusing information from previous centres, which is rarely
what an interviewer is after.
""",
    "word-search": """
Depth-first search from every cell, matching one character per step and marking the current cell as
used so a path cannot reuse it.

The mark must be undone on the way back out, otherwise later paths see cells as blocked. Writing a
sentinel like `'#'` into the board and restoring it afterwards avoids a separate visited set.

Worst case `O(m * n * 4^L)`; the early exit on a character mismatch is what keeps it fast in
practice.
""",
    "longest-increasing-subsequence": """
The `O(n^2)` DP — for each index, scan everything before it — is the natural first answer.

The `O(n log n)` version keeps a `tails` array where `tails[k]` is the smallest possible tail of an
increasing subsequence of length `k + 1`. For each value, binary search for the first tail that is
not smaller and overwrite it, appending when the value beats every tail.

`tails` is not the subsequence itself — only its length is meaningful — but that length is the
answer.
""",
    "edit-distance": """
Classic two-dimensional DP. `dp[i][j]` is the distance between the first `i` characters of one word
and the first `j` of the other.

Equal characters cost nothing and inherit the diagonal. Otherwise the cost is one plus the best of
the three edits: replace (diagonal), delete (up), insert (left). The first row and column are just
"delete everything so far".

`O(m * n)` time; keeping only the previous row drops space to `O(min(m, n))`.
""",
    "trapping-rain-water": """
Water above a bar is limited by the tallest bar to its left and the tallest to its right, whichever
is shorter, minus the bar itself.

Precomputing those two arrays makes it obvious in `O(n)` time and `O(n)` space. Two pointers get it
to `O(1)` space: move whichever side has the smaller running maximum, because that side is the one
capping the water.

A monotonic stack solves it by filling basins layer by layer, also in linear time.
""",
    "median-of-two-sorted-arrays": """
Merging is `O(m + n)`; the intended answer is `O(log(min(m, n)))`.

Binary search a split point in the shorter array. The split is correct when every element left of
the cut in both arrays is no larger than every element right of it — check the two cross pairs.

Once the cut is right, the median comes from the boundary values: the maximum of the two lefts for
an odd total, or the average of that and the minimum of the two rights for an even one.

Using infinities for the out-of-range boundaries removes every edge case.
""",
    "merge-k-sorted-lists": """
Merging one list at a time into an accumulator is `O(k * n)` — the accumulated list gets re-walked
every round.

A min-heap holding the current head of each list fixes that: pop the smallest, append it, push its
successor. `O(n log k)` time and `O(k)` space.

Merging pairwise in rounds like a tournament gets the same `O(n log k)` with `O(1)` extra space.
""",
    "minimum-window-substring": """
Slide a window and keep a count of how many required characters are still missing.

Extend right until nothing is missing, then contract from the left while the window is still valid,
recording the smallest one seen. Each pointer only ever moves forward, so it is `O(n)`.

Letting the counts go negative is the neat trick: a character with a negative count is surplus, so
it can leave the window without making it invalid.
""",
})

EDITORIALS.update({
    "set-matrix-zeroes": """
Zeroing a row while you are still reading the matrix destroys the information you need, so the two
phases have to stay separate: find every row and column that must be cleared, then clear them.

The `O(m + n)` space version keeps two sets. The `O(1)` version stores those marks in the first row
and first column of the matrix itself, which is why those two lines need their own flags — they are
serving double duty.

`O(m * n)` time either way.
""",
    "pascals-triangle": """
Each row starts and ends with `1`, and every value in between is the sum of the two directly above
it.

Build row by row from the previous one — no factorials, no recomputation. `O(n^2)` time and `O(n^2)`
space, which is just the size of the output.
""",
    "next-permutation": """
Scan from the right for the first index `i` where `nums[i] < nums[i + 1]`. Everything after `i` is
non-increasing, meaning it is the largest arrangement of those values and cannot be advanced.

Swap `nums[i]` with the rightmost value greater than it, then reverse the suffix — the suffix was
descending, so reversing makes it the smallest arrangement, giving the *next* permutation rather
than a later one.

No `i` means the whole array is descending, so reversing it yields the smallest permutation.
`O(n)` time, `O(1)` space.
""",
    "sort-colors": """
The Dutch national flag partition. Three pointers: `low` marks the end of the zeroes, `high` marks
the start of the twos, and `mid` scans.

A `0` swaps to `low` and both `low` and `mid` advance. A `1` just advances `mid`. A `2` swaps to
`high` and `high` retreats — `mid` does **not** advance, because the value swapped in from the back
has not been examined yet.

One pass, `O(n)` time, `O(1)` space.
""",
    "merge-intervals": """
Sort by start time. After that, an interval either overlaps the last one kept — in which case
extend that one's end — or it starts a new group.

Taking the maximum of the two ends matters: an interval can be entirely swallowed by the previous
one, and blindly assigning its end would shrink the result.

`O(n log n)` for the sort, `O(n)` afterwards.
""",
    "insert-interval": """
The input is already sorted and disjoint, so the work splits into three runs: intervals that end
before the new one starts (copy), intervals that overlap it (absorb into one), and intervals that
start after it ends (copy).

The absorbed run collapses into a single interval spanning the minimum start and maximum end. One
pass, `O(n)` time — no sorting needed.
""",
    "non-overlapping-intervals": """
This is interval scheduling: keeping the most intervals is the same as removing the fewest.

Sort by **end** time and greedily keep every interval that starts at or after the last kept end.
Finishing earliest leaves the most room for what follows, which is why sorting by end beats sorting
by start.

`O(n log n)` time, `O(1)` extra space.
""",
    "find-the-duplicate-number": """
Read the array as a function: index `i` points at index `nums[i]`. Because values are in `[1, n]`
and there are `n + 1` of them, two indices point at the same place — the sequence has a cycle.

Floyd's tortoise and hare finds the meeting point, then resetting one pointer to the start and
advancing both one step at a time lands on the cycle entrance, which is the duplicate.

`O(n)` time, `O(1)` space, and the array is never modified.
""",
    "missing-and-repeating-number": """
Two unknowns need two equations. The difference of actual and expected sums gives
`repeating - missing`; the difference of squared sums gives `(repeating - missing)(repeating +
missing)`, so dividing recovers `repeating + missing`.

Add and halve for the repeating value, subtract for the missing one. `O(n)` time, `O(1)` space.

XOR of all values and all indices gives a bitwise version: the result is `repeating ^ missing`, and
any set bit in it splits the numbers into two groups that each contain one of them.
""",
    "count-inversions": """
Brute force is `O(n^2)`. Merge sort counts them for free: while merging two sorted halves, every
time an element is taken from the right half, it is smaller than *all* remaining elements in the
left half — add that many inversions at once.

Inversions within each half come from the recursive calls, so the totals add up cleanly.
`O(n log n)` time, `O(n)` space.

A Fenwick tree over compressed values gives the same complexity by counting, for each element, how
many larger values came before it.
""",
    "search-a-2d-matrix": """
The rows are sorted and each row starts after the previous one ends, so the matrix is a single
sorted sequence that happens to be stored in two dimensions.

Binary search indices `0` to `m * n - 1` and map index `k` to `matrix[k // cols][k % cols]`.
`O(log(m * n))` time, `O(1)` space.

Two separate searches — first for the row, then inside it — cost the same and are easier to get
wrong.
""",
    "majority-element-ii": """
At most two values can each occupy more than a third of the array, so extend Boyer-Moore voting to
two candidates and two counters.

Match a candidate and increase its counter; find an empty counter and adopt the value; otherwise
decrement both. Cancelling in threes is what makes the bound work.

Voting only shortlists — the second pass that counts the two survivors is mandatory, because
without a guarantee that majorities exist, the candidates can be noise. `O(n)` time, `O(1)` space.
""",
    "reverse-pairs": """
Same shape as counting inversions, but the condition `nums[i] > 2 * nums[j]` is not the merge
comparison, so the counting cannot ride along inside the merge.

Do it in two stages per recursion: with both halves sorted, sweep a pointer across the right half
for each element of the left half to count the qualifying pairs, then merge normally.

Each level does `O(n)` counting work and there are `log n` levels, so `O(n log n)` overall.
""",
    "4sum": """
Sort, fix two indices with nested loops, and two-point the remaining range — the same ladder as
3Sum with one more rung.

Skipping duplicate values at every level is what keeps the output unique. Two extra prunes help a
lot in practice: break out when the smallest possible sum from here already exceeds the target, and
skip ahead when the largest possible sum is still below it.

`O(n^3)` time, `O(1)` space beyond the sort.
""",
    "longest-subarray-with-sum-zero": """
If two prefix sums are equal, the stretch between those two positions sums to zero.

Walk the array keeping a running sum and a map from sum to the **first** index where it appeared.
Keeping the earliest index is what makes the span longest. A prefix sum of zero means the subarray
starts at index 0, which is why the map is seeded with `{0: -1}`.

`O(n)` time, `O(n)` space.
""",
    "count-subarrays-with-given-xor": """
XOR behaves like addition here: the XOR of `nums[i..j]` is `prefix[j] ^ prefix[i - 1]`.

So for the current prefix `x`, the subarrays ending here with XOR `k` are exactly those starting
after a previous prefix equal to `x ^ k`. Keep a map of prefix counts and add the matching count at
each step.

Seed the map with `{0: 1}` for subarrays that start at index 0. `O(n)` time, `O(n)` space.
""",
    "container-with-most-water": """
Start with the widest possible container and walk the two pointers inwards.

The area is limited by the shorter of the two lines, so moving the taller one can never help: width
shrinks and the height is still capped by the same short line. Moving the shorter one is the only
move that can improve anything, which is why greedily discarding it is safe.

`O(n)` time, `O(1)` space.
""",
    "max-consecutive-ones": """
One counter for the current run and one for the best seen. Every `1` extends the run, every `0`
resets it to zero.

`O(n)` time, `O(1)` space. The follow-up versions of this problem — allowing one or `k` flips —
turn it into a sliding window, which is the more interesting exercise.
""",
    "remove-duplicates-from-sorted-array": """
Because the array is sorted, duplicates are adjacent, so a write pointer trailing a read pointer is
enough.

The read pointer scans; whenever it finds a value different from the last one written, that value is
copied to the write position and the write pointer advances. Everything past the write pointer is
leftover junk, which is why the count is the return value.

`O(n)` time, `O(1)` space.
""",
    "maximum-product-subarray": """
Kadane's algorithm does not transfer directly, because multiplying by a negative flips the ranking:
the most negative product becomes the largest one.

So track two running values — the maximum and the minimum product ending at the current index — and
recompute both from the three candidates `value`, `max * value`, `min * value`.

Zeroes reset both, which the same three-candidate rule handles automatically. `O(n)` time, `O(1)`
space.
""",
    "find-minimum-in-rotated-sorted-array": """
Compare the middle element with the **right** end. If the middle is larger, the rotation point must
be to its right, so move `lo` past it; otherwise the middle could itself be the minimum, so move
`hi` to it.

Comparing with the left end instead needs an extra case for the already-sorted array — the right
end is the cleaner invariant.

`O(log n)` time, `O(1)` space.
""",
    "valid-palindrome": """
Two pointers walking inwards, each skipping anything that is not alphanumeric, comparing
case-folded characters.

Building a cleaned copy first is fine and costs `O(n)` extra space; the two-pointer version keeps it
at `O(1)`.

`O(n)` time. The pointers must be advanced *inside* the skip branches, or a string of punctuation
loops forever.
""",
    "longest-common-prefix": """
Compare the strings column by column and stop at the first mismatch or the first string that runs
out. The answer can never be longer than the shortest string, so that one bounds the loop.

`O(total characters)` in the worst case, `O(1)` extra space.

Sorting the array and comparing only the first and last string works too, since everything between
them shares at least that prefix.
""",
    "roman-to-integer": """
The subtractive cases (`IV`, `IX`, `XL`, ...) all share one rule: a numeral smaller than the one
after it is subtracted rather than added.

So walk left to right, look one character ahead, and pick the sign. No special-casing of the six
pairs required. `O(n)` time, `O(1)` space.
""",
    "string-to-integer-atoi": """
A small state machine: skip spaces, read an optional sign, then consume digits until something else
appears.

The clamp is the real exercise. Check the bound *before* the value overflows — after multiplying by
ten it is already too late in fixed-width languages. Comparing against `INT_MAX / 10` before each
step, or clamping as soon as the running value passes the limit, both work.

Anything unparsed at the front means the answer is `0`; anything after the digits is ignored.
""",
    "add-two-numbers": """
The digits are stored in reverse, which is exactly the order addition wants: least significant
first.

Walk both lists together with a carry, creating one output node per step. Guard the loop on
`l1 or l2 or carry` so a final carry gets its own node — `999 + 1` is the case that catches people.

A dummy head removes the special case for the first node. `O(m + n)` time, `O(1)` extra space.
""",
    "middle-of-the-linked-list": """
Slow and fast pointers: the fast one moves two steps for every one the slow one takes, so when it
falls off the end, the slow one is halfway.

Looping while `fast and fast.next` returns the **second** middle for even lengths, which is what
this problem asks for; looping while `fast.next and fast.next.next` returns the first.

`O(n)` time, `O(1)` space, one pass — no length count needed.
""",
    "remove-nth-node-from-end-of-list": """
Send one pointer `n` nodes ahead, then advance both together. When the leader reaches the last node,
the trailing pointer is sitting just before the node to remove.

Starting both at a dummy head makes removing the first node identical to removing any other, which
is the whole reason the dummy exists.

`O(n)` time, one pass, `O(1)` space.
""",
    "delete-node-in-a-linked-list": """
The point of the original problem is that you only get the node itself — you can never reach its
predecessor, so the pointer into it cannot be rerouted.

The trick is to stop thinking about deleting the node and start thinking about deleting its
*value*: copy the next node's value into this one, then unlink the next node. The list looks
identical afterwards.

`O(1)` time and space, and it is exactly why the node is guaranteed not to be the tail.
""",
    "intersection-of-two-linked-lists": """
The lists have different lengths, so the naive walk misaligns. Switching lists at the end fixes it:
a pointer that walks `A` then `B`, and another that walks `B` then `A`, both travel `lenA + lenB`
steps and therefore arrive at the join together.

If the lists never intersect, both hit the end at the same moment and the loop ends with nulls.

`O(m + n)` time, `O(1)` space — no hash set of visited nodes needed.
""",
    "linked-list-cycle": """
Floyd's tortoise and hare: one pointer moves one step, the other two.

If there is a cycle, the fast pointer laps the slow one and they meet — the gap between them shrinks
by exactly one node per step, so a meeting is guaranteed. If there is no cycle, the fast pointer
runs off the end.

`O(n)` time, `O(1)` space, and it does not modify the list the way a visited-set or
mark-as-you-go approach would.
""",
    "linked-list-cycle-ii": """
Run tortoise and hare until they meet, then reset one pointer to the head and advance both one step
at a time — they meet again exactly at the cycle entrance.

The reason is arithmetic: if the tail before the cycle is length `a` and the meeting point is `b`
into a cycle of length `c`, then `a` and `c - b` are congruent modulo `c`, so both pointers cover
the same distance to the entrance.

`O(n)` time, `O(1)` space.
""",
    "palindrome-linked-list": """
Copying values into an array makes this trivial in `O(n)` space. The constant-space version does
three things: find the middle with slow/fast pointers, reverse the second half in place, then walk
the two halves in lockstep.

Compare until the reversed half runs out — with an odd length the middle node belongs to both halves
and never needs checking.

`O(n)` time, `O(1)` space. Politeness suggests restoring the list afterwards.
""",
    "reverse-nodes-in-k-group": """
Handle one group at a time, and check *before* reversing that `k` nodes actually remain — a short
trailing group must be left untouched, so the check cannot come afterwards.

Keep a pointer to the tail of the previously finished group so each reversed block can be stitched
back in. Reversing a block is the standard three-pointer walk, stopped at the node after the group.

`O(n)` time, `O(1)` space.
""",
    "rotate-list": """
Rotating right by `k` moves the last `k` nodes to the front. Walk the list once to get its length
and its tail, then close it into a ring.

Reduce `k` modulo the length — `k` can be far bigger than the list — and cut the ring
`length - k % length` nodes after the head. `O(n)` time, `O(1)` space.

Forgetting to null out the new tail leaves the list circular and the checker hanging.
""",
    "reorder-list": """
Three familiar pieces bolted together: split the list at the middle with slow/fast pointers, reverse
the second half, then weave the two halves alternately.

Cutting the first half loose (setting `slow.next = None`) before reversing is what stops the weave
from looping back into itself.

`O(n)` time, `O(1)` space. Pushing everything into an array and re-linking by index is the same
result with `O(n)` memory.
""",
    "copy-list-with-random-pointer": """
A hash map from original node to its copy makes this a two-pass, `O(n)`-space exercise: create the
copies, then wire up `next` and `random` through the map.

The `O(1)`-space version interleaves the copies into the original list — `A -> A' -> B -> B'` — so
each copy is reachable from its original by a single `next` hop. Set `copy.random =
node.random.next`, then unzip the two lists apart.

The unzip must fully restore the original list, not just extract the copy.
""",
    "flatten-a-linked-list": """
Every column is already sorted, so this is k-way merging with `bottom` pointers instead of `next`.

Recursing to the right first and merging backwards means each merge folds one column into an
already-flattened tail, so the merge routine only ever handles two sorted lists.

With `n` columns of `m` nodes it is `O(n * m)` per merge in the worst case; a heap over the column
heads gives `O(total log n)` if the columns are many.
""",
})

EDITORIALS.update({
    "binary-tree-inorder-traversal": """
Recursively it is three lines: left, node, right. The iterative version is the one worth knowing.

Push left children onto a stack until there are none, pop a node and record it, then move to its
right child and repeat. The stack holds exactly the ancestors whose right subtrees are still
pending.

`O(n)` time, `O(h)` space. Morris traversal removes even that stack by threading the tree.
""",
    "binary-tree-preorder-traversal": """
Node, then left, then right. Iteratively, push the root and pop in a loop, pushing the **right**
child before the left so the left comes off first.

`O(n)` time, `O(h)` space in the typical case — the stack holds at most one branch's worth of
pending right children.
""",
    "binary-tree-postorder-traversal": """
Left, right, node — awkward iteratively because a node must wait for both subtrees.

The one-stack trick: run a preorder variant that visits node, **right**, left, then reverse the
whole output. That reversed sequence is exactly postorder.

`O(n)` time, `O(n)` space for the output. The two-stack version is the same idea written more
explicitly.
""",
    "binary-tree-zigzag-level-order-traversal": """
Do a plain level-order traversal and reverse every other level. Reversing a level costs `O(width)`,
which does not change the overall `O(n)`.

Alternating a deque and pushing children in a different order works too, but it is easy to get the
child order backwards; reversing after the fact is harder to break.
""",
    "binary-tree-right-side-view": """
The visible node at each depth is the last one in that level's BFS order — so run a level-order
traversal and take the final node of every level.

The DFS version visits the right child first and records a node whenever the current depth is deeper
than anything recorded so far. Same `O(n)` time, `O(h)` stack instead of `O(width)` queue.
""",
    "top-view-of-binary-tree": """
Assign each node a horizontal distance: root is `0`, left child is `d - 1`, right child is `d + 1`.
The visible node at a distance is the shallowest one there.

BFS visits nodes in depth order, so the **first** node seen at each distance is the answer — record
it and ignore the rest. Sort the distances at the end to read left to right.

A DFS needs an explicit depth comparison, because it can reach a deeper node at a distance before a
shallower one.
""",
    "bottom-view-of-binary-tree": """
Same horizontal-distance bookkeeping as the top view, with the opposite rule: overwrite the entry
for a distance every time, so the last node BFS reaches there wins.

`O(n)` time plus the sort of the distance keys. Using an ordered map keyed by distance skips the
final sort.
""",
    "vertical-order-traversal-of-a-binary-tree": """
Group by column, but the tie-break is the whole difficulty: nodes in the same column and the same
row must be ordered by value, not by traversal order.

Collect `(column, row, value)` triples in one walk, sort them, then group by column. Sorting handles
all three keys at once, which is much less error-prone than trying to keep a BFS in the right order.

`O(n log n)` time, `O(n)` space.
""",
    "boundary-traversal-of-binary-tree": """
Three separate walks are far easier to get right than one clever traversal: the left edge from the
top down, every leaf left to right, then the right edge from the bottom up.

The rules that keep nodes from appearing twice: leaves are excluded from both edge walks, and the
root counts as part of the left boundary only when it is not itself a leaf.

Each walk is `O(h)` or `O(n)`, so the whole thing is `O(n)`.
""",
    "binary-tree-maximum-path-sum": """
Two different quantities are in play, and confusing them is the usual bug. What a node **returns**
to its parent is the best single downward path through it — value plus the better child. What a node
**contributes to the answer** is value plus *both* children, since a path may turn at this node.

Clamp negative child contributions to zero: a branch that hurts is simply not taken.

`O(n)` time, `O(h)` stack, with the global best tracked outside the recursion.
""",
    "diameter-of-binary-tree": """
The longest path through a node uses the full height of both its subtrees, so while computing
heights, record `leftHeight + rightHeight` at every node and keep the maximum.

Computing height separately for each node is `O(n^2)`; folding it into one post-order pass makes it
`O(n)` with `O(h)` stack. The answer is measured in edges, which is why heights are added and not
incremented again.
""",
    "balanced-binary-tree": """
Checking `isBalanced` at every node re-walks the subtrees and degrades to `O(n^2)`.

Instead have one post-order pass return the height, using a sentinel like `-1` to mean "already
unbalanced". As soon as a subtree reports the sentinel, propagate it without further work.

`O(n)` time, `O(h)` stack.
""",
    "lowest-common-ancestor-of-a-binary-tree": """
Recurse and return the first node that matches either target, or the node where the two targets come
back from different sides.

If both children return something, the current node is the split point and therefore the answer. If
only one child does, pass it upwards. Returning a node the moment it matches works because an
ancestor counts as a descendant of itself.

`O(n)` time, `O(h)` stack.
""",
    "same-tree": """
Two trees match when both roots are null, or both exist with equal values and both pairs of subtrees
match.

Handle the null cases first — comparing `p.val` before checking that `p` exists is the classic
crash. `O(n)` time, `O(h)` stack.
""",
    "symmetric-tree": """
Symmetry is not a property of one node, it is a property of two: compare the left subtree with the
right subtree, walking them in **opposite** directions.

So the recursion takes two nodes and checks `a.left` against `b.right` and `a.right` against
`b.left`. Comparing a tree with its own mirror image is the same algorithm with an extra copy.

`O(n)` time, `O(h)` stack.
""",
    "subtree-of-another-tree": """
At every node of the big tree, run the same-tree check against the candidate subtree. That is
`O(m * n)` in the worst case and completely acceptable here.

The linear-time version serialises both trees with explicit null markers and asks whether one
string contains the other — with a proper string-matching algorithm, `O(m + n)`. The null markers
are essential, otherwise unrelated shapes serialise identically.
""",
    "root-to-node-path-in-binary-tree": """
Plain backtracking: push the current value on the way down, recurse into both children, and pop when
neither subtree found the target.

The recursion returns a boolean so the first success short-circuits and the path is left intact on
the stack. `O(n)` time, `O(h)` space.
""",
    "maximum-width-of-binary-tree": """
Index the nodes like a heap: a node at index `i` has children `2i` and `2i + 1`. The width of a
level is then `lastIndex - firstIndex + 1`, counting the missing nodes in between.

Subtract the level's first index from every node's index as you go, or the numbers grow
exponentially and overflow on deep, sparse trees.

`O(n)` time, `O(width)` space.
""",
    "children-sum-property": """
Two passes folded into one recursion. On the way down, push the parent's value into its children
(setting each child to at least the parent's value) so the children can afford whatever the parent
claims — values may only increase.

On the way back up, set the parent to the sum of its (now final) children. Leaves are left alone,
which anchors the recursion.

`O(n)` time, `O(h)` stack.
""",
    "all-nodes-distance-k-in-binary-tree": """
Distance runs upwards too, so the tree has to be treated as an undirected graph. One walk records
every node's parent; after that, each node has up to three neighbours.

Then it is a plain BFS from the target, level by level, stopping when the level index reaches `k`.
A visited set is required — without it the search bounces back and forth between a node and its
parent.

`O(n)` time and space.
""",
    "minimum-time-to-burn-a-tree": """
Same shape as "nodes at distance k", but instead of stopping at a level, the answer is the *last*
level reached.

Record parents, BFS outward from the burning node counting levels, and return the final count. Start
the counter at `-1` so a single-node tree answers `0`.

`O(n)` time and space.
""",
    "count-complete-tree-nodes": """
Walking every node is `O(n)` and misses the point. In a complete tree, compare the depth of the
leftmost path with the depth of the rightmost path: if they match, the subtree is perfect and holds
exactly `2^h - 1` nodes — no recursion needed.

Otherwise recurse into both children. Only one child per level is ever imperfect, so the recursion
does `O(log n)` real work, each step costing `O(log n)` to measure depths: `O(log^2 n)` overall.
""",
    "flatten-binary-tree-to-linked-list": """
The target order is preorder, so the natural solutions run preorder backwards.

The `O(1)`-space version threads the tree: for each node with a left child, find the rightmost node
of that left subtree, point it at the current right subtree, then move the left subtree over to the
right and null the left pointer. Move to the new right child and repeat.

`O(n)` time — each edge is walked at most twice.
""",
    "morris-inorder-traversal": """
The trick is to borrow the unused right pointers of leaves as temporary threads back to their
successors.

At each node with a left child, find that subtree's rightmost node. If its right pointer is empty,
set it to the current node and descend left. If it already points back here, the left subtree is
finished — remove the thread, record the value, and go right.

`O(n)` time, `O(1)` space, and the tree is restored exactly as it was.
""",
    "populating-next-right-pointers-in-each-node": """
A BFS solves it in `O(width)` memory. The constant-space version uses the `next` pointers of the
level above as its own queue.

Walk the current level through the pointers you already set, wiring together the children as you go
and remembering the leftmost child to start the next level. Nothing is stored beyond a few pointers.

`O(n)` time, `O(1)` space.
""",
    "search-in-a-binary-search-tree": """
One comparison per level: smaller values are to the left, larger to the right. Walk down until the
value matches or the pointer falls off the tree.

`O(h)` time — `O(log n)` on a balanced tree, `O(n)` on a degenerate one — and `O(1)` space when
written iteratively.
""",
    "convert-sorted-array-to-binary-search-tree": """
Taking the middle element as the root splits the remaining values evenly, which is exactly what
keeps the tree balanced. Recurse on the two halves.

`O(n)` time, `O(log n)` stack. Several trees are valid in general; fixing the middle index as
`(lo + hi) // 2` makes the output deterministic, which is what this checker compares against.
""",
    "construct-bst-from-preorder-traversal": """
Preorder gives the root first, and the BST property tells you where the split is — everything below
the root value belongs to the left subtree.

Scanning for that split each time is `O(n^2)`. The linear version carries an upper bound down the
recursion: consume values while they stay under the bound, building the left subtree with the node's
own value as the new bound and the right subtree with the inherited one.

`O(n)` time, `O(h)` stack.
""",
    "lowest-common-ancestor-of-a-binary-search-tree": """
Ordering makes this much easier than the general tree version: if both values are smaller than the
current node, the answer is to the left; if both are larger, to the right.

The first node where the values fall on opposite sides — or where one of them equals the node — is
the lowest common ancestor.

`O(h)` time, `O(1)` space iteratively.
""",
    "inorder-predecessor-and-successor": """
Two independent descents, each recording a candidate whenever it moves away from it.

For the successor, go left whenever the node's value is greater than the key (recording that node)
and right otherwise. For the predecessor, mirror it. The key does not have to exist in the tree,
which is why this beats "find the node, then look at its subtree".

`O(h)` time, `O(1)` space.
""",
    "floor-and-ceil-in-bst": """
Same shape as predecessor and successor, but the bounds are inclusive — an exact match is both the
floor and the ceiling, so it can short-circuit.

Walk down once, recording the last value that was at most the key (floor) and the last value that
was at least the key (ceiling). `O(h)` time, `O(1)` space.
""",
    "kth-smallest-element-in-a-bst": """
An inorder traversal of a BST emits values in sorted order, so run one and stop after `k` of them.

The iterative stack version is what makes the early exit natural — `O(h + k)` time rather than a
full `O(n)` walk.

If the tree is modified often, storing a subtree size in each node turns each query into an `O(h)`
descent.
""",
    "two-sum-iv-input-is-a-bst": """
A hash set of visited values reduces it to plain two-sum during any traversal: `O(n)` time and
space, and it ignores the BST property entirely.

The version that uses the ordering runs two iterators — one inorder (ascending), one reverse-inorder
(descending) — and moves them like two pointers on a sorted array. That is `O(n)` time with `O(h)`
space.

The two pointers must never cross, otherwise a single node pairs with itself.
""",
    "binary-search-tree-iterator": """
Flattening the tree in the constructor makes `next` trivial but costs `O(n)` memory, which the
problem rules out.

Keep a stack holding the leftmost spine instead. `next` pops a node and then pushes the left spine
of its right subtree. Each node is pushed and popped exactly once across the whole traversal, so
`next` is `O(1)` amortised with `O(h)` memory.
""",
    "largest-bst-in-a-binary-tree": """
Checking each subtree independently is `O(n^2)`. One post-order pass fixes that if every node
reports four things about its subtree: size, minimum, maximum, and whether it is a BST.

A node forms a BST when both children do and its value sits strictly between the left subtree's
maximum and the right subtree's minimum. Empty subtrees report `+inf` and `-inf` so leaves work
without special cases.

`O(n)` time, `O(h)` stack.
""",
    "maximum-sum-bst-in-binary-tree": """
Identical bookkeeping to the largest-BST problem, with the subtree sum carried alongside the bounds.

The one wrinkle is negatives: an all-negative BST is worse than taking nothing, and since the empty
subtree is a valid BST with sum zero, the answer never drops below zero.

`O(n)` time, `O(h)` stack.
""",
    "binary-tree-to-doubly-linked-list": """
Inorder order is exactly the sorted order the list needs, so do an inorder walk and relink as you
go: keep a pointer to the previously visited node, set `prev.right = node` and `node.left = prev`.

The first node visited becomes the head. Finish by nulling the head's `left` and the tail's `right`
so the list has real ends.

`O(n)` time, `O(h)` stack.
""",
    "construct-binary-tree-from-preorder-and-inorder-traversal": """
The first preorder value is the root. Finding it in the inorder array splits that array into the
left and right subtrees, and their sizes tell you how much of the preorder array belongs to each.

Scanning for the root each time is `O(n^2)`; a value-to-index map over the inorder array makes it
`O(n)`. Consume preorder values with a single moving index rather than slicing.

`O(n)` time, `O(n)` space.
""",
    "construct-binary-tree-from-inorder-and-postorder-traversal": """
Postorder ends with the root, so consume it from the **back** and build the right subtree before the
left — the mirror image of the preorder version.

Same value-to-index map over the inorder array for the split, same `O(n)` result. Building the left
subtree first with a backwards index is the bug that produces a mirrored tree.
""",
    "serialize-and-deserialize-binary-tree": """
Any format works as long as it records the shape as well as the values, which means null children
need explicit markers.

Preorder with a `#` for each null is the shortest thing that works: deserialising is a recursion
that consumes tokens in the same order, returning null on a marker. A level-order format with
markers is equally valid and easier to read by eye.

`O(n)` for both directions.
""",
})

EDITORIALS.update({
    "sum-of-two-integers": """
Addition splits into two halves: `a ^ b` adds every column while ignoring carries, and `(a & b) << 1`
is exactly the carries. Repeat until there is no carry left.

In languages with fixed 32-bit integers this is the whole answer. In Python, integers are unbounded,
so mask to 32 bits each round and convert back to a signed value at the end — otherwise negative
results loop forever.
""",
    "number-of-1-bits": """
`n & (n - 1)` clears the lowest set bit — subtracting one flips that bit and everything below it, so
the AND wipes it out. Loop until `n` is zero and count the iterations.

That runs once per set bit instead of once per bit position: `O(popcount)` rather than `O(32)`.
Every mainstream language also has a built-in for this, which is what real code should use.
""",
    "counting-bits": """
Every number is a smaller number shifted left, plus its own last bit:
`bits[i] = bits[i >> 1] + (i & 1)`.

That makes one `O(n)` pass enough, with no per-number bit loop. The alternative recurrence
`bits[i] = bits[i & (i - 1)] + 1` says the same thing from the "clear the lowest bit" angle.
""",
    "reverse-bits": """
Shift the answer left, take the lowest bit of the input, OR it in, shift the input right. Thirty-two
times, regardless of value.

`O(1)` time and space. The divide-and-conquer version swaps halves, then quarters, then bytes with
fixed masks — five operations instead of a loop, and the standard follow-up when the function is
called repeatedly.
""",
    "missing-number": """
XOR everything together: all the indices `0..n` and all the values. Every number that is present
appears exactly twice and cancels; the missing one is left standing.

`O(n)` time, `O(1)` space, and no overflow risk. The Gauss sum — `n(n + 1) / 2` minus the actual
sum — is equally short but can overflow in fixed-width languages.
""",
    "powx-n": """
Fast exponentiation: `x^n` is `(x^2)^(n/2)` for even `n`, and `x * x^(n-1)` for odd `n`. Each step
halves the exponent, so it finishes in `O(log n)` multiplications.

Negative exponents invert the base and negate the exponent — but negating `INT_MIN` overflows in
fixed-width languages, which is the trap in this problem.
""",
    "nth-root-of-a-number": """
The `n`-th root is monotone in the candidate, so binary search `k` in `[1, m]` and compare `k^n`
with `m`.

Computing `k^n` naively overflows fast; stop multiplying the moment the running product passes `m`,
since that already answers the comparison.

`O(n log m)` time, `O(1)` space.
""",
    "single-element-in-a-sorted-array": """
XOR-ing everything gives the answer in `O(n)`, but the array is sorted, so `O(log n)` is available.

Before the single element, every pair starts at an even index; after it, pairs start at odd indices.
Force the midpoint to an even index and compare it with its neighbour: if they match, the single
element is to the right; if not, it is at the midpoint or to the left.

`O(log n)` time, `O(1)` space.
""",
    "kth-element-of-two-sorted-arrays": """
Merging until the `k`-th element is `O(k)`. The binary search version is `O(log(min(m, n)))`.

Search the number of elements taken from the shorter array; the rest come from the longer one. The
split is correct when both left-side maxima are no larger than both right-side minima — then the
answer is the larger of the two left maxima.

Infinities for the out-of-range boundaries remove the edge cases at the ends.
""",
    "allocate-minimum-pages": """
Binary search the answer, not the arrangement. Candidate answers run from the largest single book —
someone has to read it — to the sum of all pages, which is one reader taking everything.

For a candidate limit, greedily fill one reader until the next book would exceed it, then start a
new reader. Fewer readers needed than allowed means the limit can shrink.

`O(n log(sum))` time. Fewer books than readers is impossible, hence the `-1`.
""",
    "aggressive-cows": """
The same shape as allocating pages: binary search the minimum distance, and check feasibility
greedily.

For a candidate distance, place the first cow in the first stall and then take every stall at least
that far from the last placement. If all cows fit, the distance can grow.

Sorting the stalls first is what makes the greedy check valid. `O(n log(max position))`.
""",
    "matrix-median": """
Building the flat array is `O(r * c)` memory and `O(r * c log(r * c))` time. Binary searching the
**value** avoids both.

For a candidate value, count entries less than or equal to it — one upper-bound search per sorted
row. The median is the smallest value whose count exceeds half the total.

`O(32 * r * log c)` time, `O(1)` space, and it only needs each row sorted, not the whole matrix.
""",
    "n-meetings-in-one-room": """
Classic activity selection: sort by finishing time and take every meeting that starts after the last
one ended.

Finishing earliest leaves the most room for everything after it — sorting by start time or by
duration both produce counterexamples.

`O(n log n)` time, `O(n)` space for the sort.
""",
    "minimum-platforms": """
Trains do not need to be tracked individually — only the number of overlaps at any moment matters.

Sort arrivals and departures separately and sweep them like a merge: an arrival before the next
departure needs one more platform, otherwise a platform frees up. The running maximum is the answer.

`O(n log n)` time, `O(1)` extra space. Ties count as an overlap, which is the "arrives exactly as
another leaves" case.
""",
    "job-sequencing-problem": """
Greedy by profit: consider jobs from most valuable to least, and place each in the **latest** free
slot before its deadline. Taking a late slot preserves the early ones for jobs with tighter
deadlines.

Scanning backwards for a free slot is `O(n * maxDeadline)`; a disjoint-set that points each filled
slot at the next free one below it makes each placement near-constant.

`O(n log n)` overall, dominated by the sort.
""",
    "fractional-knapsack": """
Fractions make the greedy choice optimal: sort by value per unit weight and fill from the top. Only
the final item is ever split, and it contributes proportionally.

The 0/1 version cannot do this — that is why it needs dynamic programming.

`O(n log n)` time, `O(1)` extra space.
""",
    "assign-cookies": """
Sort both lists and walk them with two pointers, matching the smallest sufficient cookie to the least
hungry child.

Spending a bigger cookie on a small appetite can only waste it, which is why the greedy match is
optimal. `O(n log n)` time, `O(1)` extra space.
""",
    "minimum-coins": """
The Indian denominations are canonical, meaning the greedy choice is provably optimal: take as many
of the largest note as fit, then move down.

That is not true for arbitrary coin systems — `[1, 3, 4]` making `6` is the standard
counterexample, and that is when dynamic programming becomes necessary.

`O(denominations)` time, `O(1)` space.
""",
    "meeting-rooms": """
Sort by start time and compare each meeting with the previous end. Any overlap means the answer is
false.

`O(n log n)` time, `O(1)` extra space. Meetings that merely touch at an endpoint do not overlap,
which is why the comparison is strict.
""",
    "meeting-rooms-ii": """
The answer is the maximum number of meetings in progress at once.

A min-heap of end times models the rooms directly: reuse the earliest-finishing room when it frees
before the next meeting starts, otherwise open a new one. The heap size is the answer.

The sweep-line version sorts starts and ends separately and tracks the running overlap — same
`O(n log n)`, no heap.
""",
    "longest-common-subsequence": """
`dp[i][j]` is the answer for the first `i` characters of one string and the first `j` of the other.
Equal characters extend the diagonal by one; otherwise take the better of dropping a character from
either string.

`O(m * n)` time. Only the previous row is ever read, so one rolling array gives `O(min(m, n))`
space — but reconstructing the actual subsequence needs the full table.
""",
    "0-1-knapsack": """
`best[c]` is the best value achievable with capacity `c` using the items processed so far.

Iterating capacities **downwards** for each item is what enforces "at most once": going upwards
would let an item be picked up again in the same pass, which is the unbounded knapsack instead.

`O(n * capacity)` time, `O(capacity)` space.
""",
    "subset-sum-equal-to-target": """
The same table as knapsack, storing reachability instead of value: `reachable[t]` means some subset
sums to `t`.

Process each value once and update the sums downwards so a value cannot be reused. `O(n * target)`
time, `O(target)` space.

A bitset makes this dramatically faster in practice — shifting the whole set left by the value ORs
in every new reachable sum at once.
""",
    "count-subsets-with-given-sum": """
Same recurrence as subset sum, but counting instead of flagging: `counts[t] += counts[t - value]`.

Zeroes need care. A zero can be in or out of any subset without changing the sum, so each one
doubles every count — handling it with the normal loop would only add, and undercount.

`O(n * target)` time, `O(target)` space.
""",
    "minimum-sum-partition": """
The two subset sums add to a fixed total, so the difference is determined by either one of them.
Minimising the difference means finding the reachable subset sum closest to half the total.

Run the subset-sum DP up to `total / 2`, then take the largest reachable value and return
`total - 2 * that`.

`O(n * total)` time, `O(total)` space.
""",
    "rod-cutting": """
Unbounded knapsack: a piece of any length may be cut any number of times.

`best[length] = max(prices[cut - 1] + best[length - cut])` over every cut that fits. Iterating
lengths upwards is what allows reuse — the mirror image of the 0/1 knapsack's downward loop.

`O(n^2)` time, `O(n)` space.
""",
    "egg-dropping": """
The textbook recurrence — minimise over drop floors the worst of "breaks" and "survives" — is
`O(eggs * floors^2)` and far too slow at these sizes.

Flip the question: with `e` eggs and `d` drops, how many floors can be *distinguished*? That is
`f(e, d) = f(e - 1, d - 1) + f(e, d - 1) + 1`. Increase `d` until the coverage reaches the building
height.

`O(eggs * answer)` time, `O(eggs)` space.
""",
    "matrix-chain-multiplication": """
Interval DP. `dp[i][j]` is the cheapest way to multiply the chain from `i` to `j`, chosen over every
split point `k` between them, paying `dims[i-1] * dims[k] * dims[j]` for the final multiplication.

Fill by increasing chain length so both halves are already solved when a longer chain needs them.

`O(n^3)` time, `O(n^2)` space.
""",
    "palindrome-partitioning-ii": """
Two layers. First precompute which substrings are palindromes — expanding around centres, or a
`O(n^2)` DP.

Then `cuts[i]` is the minimum over every `j` where `s[j..i]` is a palindrome of `cuts[j-1] + 1`, and
zero when the whole prefix is already a palindrome.

`O(n^2)` time and space. Skipping the precomputation and re-checking palindromes inside the loop
pushes it to `O(n^3)`.
""",
    "maximum-sum-increasing-subsequence": """
The longest-increasing-subsequence DP with sums instead of counts: `best[i]` is the largest sum of an
increasing subsequence ending at `i`, taken over all earlier smaller elements.

`O(n^2)` time, `O(n)` space. The `O(n log n)` trick from LIS does not transfer directly, because a
longer subsequence is not necessarily a heavier one — that needs a Fenwick tree over values.
""",
    "maximum-profit-in-job-scheduling": """
Weighted interval scheduling. Sort by end time; `best[i]` is the most profit using only the first
`i` jobs.

Each job either is skipped — inheriting the previous best — or taken, adding its profit to the best
achievable at its start time. Binary search finds the last job that finishes by then.

`O(n log n)` time, `O(n)` space. Greedy by profit fails here; unlike job sequencing, jobs have
lengths.
""",
    "house-robber-ii": """
The circle only adds one constraint: the first and last house cannot both be robbed.

So run the linear solution twice — once on houses `0..n-2`, once on `1..n-1` — and take the better
result. A single house is the one case that needs handling before the split.

`O(n)` time, `O(1)` space.
""",
    "decode-ways": """
Fibonacci-shaped: the count at position `i` is the count from taking one digit (if that digit is not
`'0'`) plus the count from taking two (if those two digits are between `10` and `26`).

Zeroes are the whole difficulty. A `'0'` cannot stand alone, so it only survives as the second half
of `"10"` or `"20"`; anything else makes the string undecodable from that point.

`O(n)` time, `O(1)` space with two rolling values.
""",
    "jump-game": """
Track the furthest index reachable so far. Walk forward; if the current index is beyond that reach,
the walk is stuck and the answer is false. Otherwise extend the reach.

`O(n)` time, `O(1)` space — no DP table needed, because reachability is monotone: if you can get
past an index, you can get to it.
""",
    "combination-sum-iv": """
Because order matters, this counts permutations, not combinations — and that decides the loop order.

The target loop must be on the **outside** and the values on the inside, so `[1, 2]` and `[2, 1]`
are both counted. Swapping the loops counts each multiset once instead, which is the
coin-change-style answer to a different question.

`O(target * n)` time, `O(target)` space.
""",
    "palindromic-substrings": """
Every palindrome has a centre, and there are `2n - 1` of them counting the gaps between characters.

Expand from each centre while the characters match and count every successful expansion — each one
is a distinct palindromic substring.

`O(n^2)` time, `O(1)` space. The DP table gives the same complexity with `O(n^2)` memory.
""",
    "longest-repeating-character-replacement": """
A window is valid when the characters that are not the most common one fit inside the replacement
budget: `windowLength - maxCount <= k`.

Slide the right edge, updating counts. When the window becomes invalid, move the left edge one step.
Letting `maxCount` go stale is safe — it only ever makes the window more conservative, and the
answer is a maximum.

`O(n)` time, `O(alphabet)` space.
""",
    "word-break-ii": """
Word Break asked whether a segmentation exists; this asks for all of them, so the answer can be
exponential in the worst case.

Recurse over prefixes, and memoise on the start index: the memo maps an index to every sentence for
the rest of the string. Without it, strings like `"aaaa...b"` re-explore the same suffix
exponentially often.

The dictionary lives in a hash set, and the length cap on `s` is what keeps the output finite.
""",
    "minimum-characters-for-palindrome": """
Adding characters only at the front means the answer is `n` minus the length of the longest
palindromic **prefix**.

Finding that in linear time is the neat part: build `s + '#' + reverse(s)` and run the KMP failure
function. Its last value is the length of the longest prefix of `s` that is also a suffix of the
reversal — exactly the longest palindromic prefix. The separator stops the match from spilling
across the join.

`O(n)` time and space.
""",
    "count-and-say": """
There is no closed form; each term is produced by run-length encoding the previous one.

Walk the string, count equal neighbours, and append the count followed by the digit. The terms grow
quickly — roughly 30% per step — which is why `n` is capped at 30.

`O(n * length of the result)` time.
""",
})

EDITORIALS.update({
    "clone-graph": """
The only real difficulty is cycles: naively recursing into neighbours revisits the node you started
from forever.

Keep a map from original node to its copy, and create the copy **before** recursing. Then a
neighbour that has already been cloned is found in the map instead of being cloned again, and the
recursion terminates.

`O(V + E)` time and space. BFS with the same map works identically.
""",
    "bfs-of-graph": """
A queue plus a visited array. The detail that matters: mark a node visited when it is **enqueued**,
not when it is dequeued — otherwise a node reachable from two places gets queued twice.

`O(V + E)` time, `O(V)` space.
""",
    "dfs-of-graph": """
Recursion or an explicit stack, visiting the first unvisited neighbour before moving on.

With an explicit stack, push neighbours in reverse order so the traversal matches the recursive one,
and check `visited` on pop as well as on push — a node can be stacked twice before it is first
expanded.

`O(V + E)` time, `O(V)` space.
""",
    "detect-cycle-in-undirected-graph": """
During a traversal, an edge back to an already visited node closes a cycle — unless it is the edge
you just came along, so the parent has to be tracked and ignored.

Union-find avoids that bookkeeping: process each edge and union its endpoints; an edge whose
endpoints already share a root closes a cycle.

`O(V + E)` with near-constant union-find operations. Parallel edges count as cycles, and the graph
may be disconnected, so every component needs checking.
""",
    "detect-cycle-in-directed-graph": """
"Already visited" is not enough here — a node can legitimately be reachable by two different paths.
A cycle is an edge back to a node still on the **current** recursion stack.

So DFS needs three colours: unvisited, in progress, finished. Kahn's algorithm answers the same
question without recursion: peel off nodes with in-degree zero, and anything left when the queue
empties sits on a cycle.

`O(V + E)` time and space.
""",
    "topological-sort": """
Kahn's algorithm: repeatedly take a node with no remaining prerequisites and relax its outgoing
edges.

Asking for the lexicographically smallest order changes only one thing — pull the smallest available
node instead of any node, which means a min-heap instead of a plain queue.

Emitting fewer than `n` nodes proves a cycle. `O((V + E) log V)` with the heap.
""",
    "is-graph-bipartite": """
Two-colour the graph during a traversal: every neighbour must get the opposite colour of the current
node, and a conflict proves it is not bipartite.

Equivalently, a graph is bipartite exactly when it contains no odd-length cycle.

Start a fresh traversal from every uncoloured node — the graph may be disconnected. `O(V + E)` time
and space.
""",
    "number-of-connected-components-in-an-undirected-graph": """
Two standard answers. Traverse from every unvisited node and count how many traversals you start; or
union every edge and count the distinct roots.

Union-find is the one that extends to edges arriving over time. Start the count at `n` and decrement
on each union that actually merges two different components.

`O(V + E)` time, `O(V)` space.
""",
    "graph-valid-tree": """
A tree is a connected acyclic graph, and on `n` nodes that forces exactly `n - 1` edges. Check the
count first — it is free and rules out most inputs.

With the right edge count, connected and acyclic imply each other, so a single union-find pass
suffices: an edge whose endpoints already share a root means a cycle, and therefore not a tree.

`O(V + E)` time, `O(V)` space.
""",
    "flood-fill": """
Depth- or breadth-first from the start pixel, spreading to neighbours that still hold the original
colour and repainting as you go.

The guard that matters: if the start pixel is already the target colour, return immediately.
Otherwise the repaint changes nothing, the neighbours still match, and the fill never terminates.

`O(m * n)` time and space.
""",
    "rotting-oranges": """
Multi-source BFS. Seed the queue with **every** rotten orange, then process the queue one level at
a time — each level is one minute.

Count the fresh oranges up front so you can tell at the end whether any are unreachable, which is
the `-1` case. A grid with no fresh oranges answers `0`, not `-1`.

`O(m * n)` time and space.
""",
    "pacific-atlantic-water-flow": """
Searching forward from every cell is `O((m * n)^2)`. Reversing the flow makes it linear.

Flood inland from each ocean's edges, moving only to neighbours of **equal or greater** height —
that is exactly the set of cells that can drain into that ocean. The answer is the intersection of
the two sets.

`O(m * n)` time and space.
""",
    "alien-dictionary": """
Each adjacent pair of words yields one ordering edge: the first position where they differ tells you
which letter comes first. Everything after that position tells you nothing.

The trap is a word followed by one of its own prefixes (`"abc"` then `"ab"`), which is impossible in
any alphabet and must return the empty string.

Then it is a topological sort over the letters seen; taking the smallest available letter at each
step makes the answer unique. `O(total characters)` time.
""",
    "dijkstras-algorithm": """
A min-heap keyed by distance. Pop the closest unfinished node, and relax its edges — with
non-negative weights, the first time a node is popped its distance is final.

Skip an entry whose recorded distance is already better than the popped one; that lazy deletion is
what makes the "decrease key" operation unnecessary.

`O((V + E) log V)` time, `O(V)` space. Negative weights break the finality argument — that is what
Bellman-Ford is for.
""",
    "bellman-ford-algorithm": """
Relax every edge `V - 1` times. Any shortest path has at most `V - 1` edges, so after that many
rounds every reachable distance is final.

One more round that still improves something proves a negative cycle, because no shortest path could
have got longer. Stopping early when a round changes nothing is a free optimisation.

`O(V * E)` time, `O(V)` space — slower than Dijkstra, but it handles negative weights.
""",
    "floyd-warshall-algorithm": """
`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`, with the intermediate node `k` on the
**outermost** loop. That order is not cosmetic: it is what lets paths through the first `k` nodes be
final before `k + 1` is considered.

Swap `-1` for infinity while working and restore it at the end. `O(V^3)` time, `O(V^2)` space, and
it gives every pair at once rather than one source.
""",
    "minimum-spanning-tree-prims": """
Grow a single tree: repeatedly take the cheapest edge that leaves the set of nodes already added.

A min-heap of candidate edges does the selection. Popping an edge whose destination is already in the
tree just skips it — the lazy version, which avoids needing a decrease-key operation.

`O((V + E) log V)` time, `O(V + E)` space. Prim's is the better fit for dense graphs, Kruskal's for
sparse ones.
""",
    "minimum-spanning-tree-kruskals": """
Sort every edge by weight and keep each one whose endpoints are not already connected.

Union-find makes the connectivity test near-constant, so the sort dominates: `O(E log E)` time,
`O(V)` space.

The correctness argument is the cut property — the lightest edge crossing any cut belongs to some
minimum spanning tree, and each kept edge is exactly that for the cut it crosses.
""",
    "strongly-connected-components": """
Kosaraju's algorithm, two passes. The first DFS records nodes by finish time; the second runs on the
**reversed** graph in reverse finish order, and each traversal there collects exactly one component.

The finish-time order is what makes it work: it visits the condensation of the graph in topological
order, so a component cannot leak into another.

`O(V + E)` time and space. Tarjan's algorithm does it in one pass with low-link values.
""",
    "word-search-ii": """
Running the single-word search once per word re-walks the board thousands of times. Put the words
into a trie and search the board **once**, descending the trie as you move.

A cell that does not match any child prunes the whole branch immediately. Removing a word from the
trie once it is found, and pruning empty nodes on the way out, stops the search from re-exploring
dead ends.

Worst case `O(m * n * 4^L)`; the trie is what makes it fast in practice.
""",
    "implement-stack-using-arrays": """
One array and one index pointing at the next free slot. Push writes and increments, pop decrements
and reads, and both check the bounds first.

`O(1)` per operation. The interesting part is the contract: a full push is dropped and an empty pop
returns a sentinel rather than throwing, so every operation is total.
""",
    "implement-queue-using-arrays": """
A naive queue shifts every element on `pop`, making it `O(n)`. A circular buffer fixes that: keep a
head index and a count, and wrap both ends with modulo arithmetic.

The array is full when the count reaches the capacity, and empty when it is zero — which is why
tracking the count is simpler than comparing head and tail indices.

`O(1)` per operation.
""",
    "implement-stack-using-queues": """
A queue gives you the oldest element, a stack needs the newest, so one of the two operations has to
do the reordering.

Making `push` expensive is the tidier choice: enqueue the new element, then rotate every earlier
element to the back. The queue front is then always the top of the stack, so `pop` and `top` are
`O(1)`.

`O(n)` push, `O(1)` everything else, one queue.
""",
    "implement-queue-using-stacks": """
Two stacks. Everything pushed goes onto the inbox; everything read comes off the outbox.

The outbox is only refilled when it runs dry, and refilling reverses the order — which is exactly
what turns LIFO into FIFO. Each element moves between the stacks at most once, so the amortised cost
per operation is `O(1)` even though a single `pop` can be `O(n)`.

Refilling on every operation instead is the version that degrades to `O(n)`.
""",
    "min-stack": """
The minimum must survive pops, so it has to be stored per element rather than as a single variable.

Push `(value, minimumSoFar)` pairs, or keep a parallel stack of minima. Either way `getMin` is a
peek.

`O(1)` per operation, `O(n)` space. The constant-space trick of encoding the previous minimum in
the stored value works but overflows easily and is rarely worth it.
""",
    "lru-cache": """
Two structures working together: a hash map for `O(1)` lookup, and a doubly linked list for `O(1)`
reordering.

The list keeps entries in recency order, so a hit unlinks its node and moves it to the front, and an
eviction always takes the tail. The map stores node references, which is what makes the unlink
constant time.

Both `get` and `put` count as a use — forgetting that on `put` of an existing key is the usual bug.

The reference below leans on Python's `OrderedDict`, which *is* a hash map over a doubly linked
list — `move_to_end` and `popitem(last=False)` are the two operations described above. In an
interview, write the linked list yourself; that is what is being asked.
""",
    "lfu-cache": """
Frequency is the primary key and recency is the tie-break, so one ordering is not enough.

Bucket keys by use count, keeping each bucket in recency order, and track the smallest non-empty
count. A hit moves a key from bucket `f` to bucket `f + 1`; an eviction takes the oldest key from
the smallest bucket.

The minimum count only ever increases on a hit or resets to one on an insert, which is what keeps
everything `O(1)`.
""",
    "online-stock-span": """
Rescanning previous days is `O(n^2)`. A monotonic stack of `(price, span)` pairs makes it linear
overall.

Any earlier day with a price at or below today's can never be the answer for a future day — today
covers it — so pop it and absorb its span. Each day is pushed once and popped once, so the amortised
cost is `O(1)`.
""",
    "kth-largest-element-in-a-stream": """
Keeping everything sorted costs `O(n)` per insertion. A min-heap capped at `k` elements does better:
push, then pop while the size exceeds `k`.

The heap then holds exactly the `k` largest values seen, and its root is the answer — `O(log k)` per
call.
""",
    "find-median-from-data-stream": """
Two heaps split the data at the median: a max-heap for the lower half, a min-heap for the upper.

Push into one, immediately move its top to the other, then rebalance so the sizes differ by at most
one. That push-and-shuffle keeps both halves correctly partitioned without comparing against the
current median.

`O(log n)` per insert, `O(1)` per query.
""",
    "next-greater-element-i": """
Sweep `nums2` once with a decreasing stack. When the current value is larger than the stack top, it
is that element's next greater — pop and record it in a map.

Then answer each query in `nums1` with a lookup, defaulting to `-1` for values still on the stack at
the end.

`O(n + m)` time, `O(n)` space, and the distinctness guarantee is what lets the map be keyed by value
rather than index.
""",
    "next-smaller-element": """
Same monotonic-stack idea, run from the right with an increasing stack.

Pop everything at least as large as the current value — those can never be the answer for anything
further left — and whatever remains on top is the next smaller element.

Each index is pushed and popped once, so it is `O(n)` time and `O(n)` space.
""",
    "sort-a-stack": """
Sorting with only stack operations is insertion sort in disguise.

Pop a value from the source, then push back everything on the sorted stack that is larger than it
before placing it — that keeps the sorted stack ordered at all times.

`O(n^2)` time, `O(n)` space. The recursive version replaces the second stack with the call stack.
""",
    "largest-rectangle-in-histogram": """
For each bar, the widest rectangle at that height runs until a strictly shorter bar on either side.
Finding both boundaries naively is `O(n^2)`.

An increasing stack of indices gives both in one sweep: when a shorter bar arrives, every taller bar
popped has found its right boundary, and its left boundary is whatever sits below it on the stack.

Appending a sentinel zero flushes the stack at the end. `O(n)` time and space.
""",
    "sliding-window-maximum": """
A heap gives `O(n log k)`; a monotonic deque gives `O(n)`.

Keep indices in the deque with decreasing values. Before adding a new index, drop every smaller value
from the back — they can never be the maximum while the new element is in the window. Drop the front
when it slides out of range.

The front is always the current maximum, and each index enters and leaves once.
""",
    "maximum-of-minimum-every-window-size": """
Turn the question around: instead of asking each window for its minimum, ask each element for the
widest window in which it is the minimum. That span is bounded by the previous and next smaller
elements, both found with a monotonic stack.

Record each element as a candidate for that span, then sweep right to left so a window of size `k`
inherits the best answer from `k + 1` — a larger window's minimum is always available to a smaller
one.

`O(n)` time and space.
""",
    "the-celebrity-problem": """
Checking every pair is `O(n^2)`. One linear pass narrows `n` candidates to one: ask whether `a`
knows `b` — if yes, `a` is disqualified, if no, `b` is.

Either way one candidate is eliminated per question, so `n - 1` questions leave exactly one
survivor. That survivor still has to be verified against everyone, because the elimination only
proves nobody *else* qualifies.

`O(n)` time, `O(1)` space.
""",
    "distinct-numbers-in-every-window": """
Maintain a count map as the window slides: add the entering element, remove the leaving one, and
delete keys whose count hits zero so the map size is the distinct count.

`O(n)` time, `O(k)` space. Recomputing a set per window is `O(n * k)` and is what this exercise
exists to replace.
""",
    "maximum-sum-combinations": """
Generating all `n^2` sums and sorting is `O(n^2 log n)` and blows up in memory.

Sort both arrays descending; the largest sum pairs the two largest values. From a pair `(i, j)`, the
next candidates are `(i + 1, j)` and `(i, j + 1)` — feed those into a max-heap and pop `k` times,
using a visited set so no pair is queued twice.

`O(n log n + k log k)` time.
""",
})

EDITORIALS.update({
    "permutations": """
Backtracking over positions: for each slot, try every value that has not been used yet, recurse, and
undo the choice.

Swapping the candidate into the current position avoids the used-array entirely — the prefix holds
the fixed choices and the suffix holds whatever is left. The swap must be undone on the way back
out.

`O(n * n!)` time, which is the size of the output, and `O(n)` extra space.
""",
    "subsets-ii": """
The plain power set is a binary choice per element. Duplicates break that: `[1, 2, 2]` would produce
the subset `[1, 2]` twice.

Sort so equal values are adjacent, then at each recursion level skip a value equal to its
predecessor — the first occurrence already generated every subset that includes "one of these".

`O(n * 2^n)` time, `O(n)` recursion depth.
""",
    "subset-sums": """
Every element is either in or out, so there are `2^n` sums and no way around generating them.

Recursing with take/skip is the direct expression. Iteratively it is even shorter: start with `[0]`
and, for each value, append that value added to every sum so far — doubling the list each round.

`O(2^n)` time and output size.
""",
    "power-set": """
Each subsequence corresponds to a bitmask from `1` to `2^n - 1`, where bit `i` decides whether
character `i` is kept.

That turns the whole problem into two nested loops with no recursion, and it naturally produces each
subsequence with characters in their original order.

`O(n * 2^n)` time — unavoidable, since that is the output size.
""",
    "combination-sum": """
Values may be reused, so the recursion has two branches at each step: take the current candidate
again (staying at the same index) or move past it for good.

Never stepping backwards is what stops `[2, 3]` and `[3, 2]` from both appearing. Sorting first
allows an early break once a candidate exceeds the remaining target.

Complexity is output-bound, roughly `O(n^(target / min))`.
""",
    "combination-sum-ii": """
Each candidate may be used once and the input may contain duplicates, so both a moving index and a
duplicate skip are needed.

Sort first. Advance the index for each recursive call so nothing is reused, and at each level skip a
value equal to its predecessor — that duplicate has already generated the same combinations from
this position.

Breaking out when a candidate exceeds the remaining target prunes most of the search.
""",
    "palindrome-partitioning": """
Try every prefix that is a palindrome, recurse on the rest, and undo the choice on the way back out.

Checking a prefix costs `O(n)` unless the palindromes are precomputed with a DP table — worth doing
if the string is long, though at these sizes the direct check is fine.

Output-bound: `O(n * 2^n)` in the worst case, `O(n)` recursion depth.
""",
    "permutation-sequence": """
Generating permutations until the `k`-th is `O(k * n)` and far too slow.

Instead notice that fixing the first digit fixes a contiguous block of `(n - 1)!` permutations. So
`(k - 1) // (n - 1)!` selects the digit, the remainder recurses into the rest, and each chosen digit
is removed from the pool.

Working with `k - 1` turns the 1-based question into 0-based arithmetic. `O(n^2)` time with a list
removal per step.
""",
    "n-queens": """
Place one queen per row and track which columns and diagonals are already attacked. A diagonal is
identified by `row - col` and an anti-diagonal by `row + col`, so both checks are set lookups.

Undo all three marks on the way back out. Building the board strings only at a complete placement
keeps the inner loop cheap.

Roughly `O(n!)` with heavy pruning, `O(n)` extra space.
""",
    "sudoku-solver": """
Backtracking with fast validity checks: keep a set of used digits per row, per column and per box,
so testing a candidate is `O(1)` rather than a scan.

Collect the empty cells once and recurse over that list — the recursion index doubles as progress,
so success is simply reaching the end.

Returning `true` up the stack the moment a full solution is found is what stops the search from
unwinding a valid board.
""",
    "m-coloring-problem": """
Colour nodes one at a time; for each, try every colour not used by an already-coloured neighbour,
recurse, and reset the colour on failure.

Failing early matters: a node with no legal colour aborts the branch immediately.

Worst case `O(m^n)`, which is why `n` is small. Ordering nodes by degree first prunes far more in
practice.
""",
    "rat-in-a-maze": """
Depth-first search from the corner, appending a move letter to the path and marking the cell as
occupied so a path cannot cross itself.

Unmark on the way back out or later paths see phantom walls. Trying the moves in the order D, L, R,
U produces the paths in lexicographic order for free.

Worst case `O(4^(n*n))`, which is why the grid stays small. A blocked start or destination means no
path at all.
""",
    "implement-trie-prefix-tree": """
Each node holds a map from letter to child plus a flag marking the end of a word.

`insert` walks and creates missing children; `search` walks and checks the flag; `startsWith` walks
and checks only that the walk survived. That flag is the whole difference between the last two.

Every operation is `O(length)` regardless of how many words are stored, which is the point of a trie
over a hash set.
""",
    "implement-trie-ii": """
Counting duplicates needs two counters per node: how many words end here, and how many pass through.

`insert` increments the passing count on every node it walks and the ending count on the last one.
`erase` decrements the same counters, which is why the word is guaranteed to be present — otherwise
the counts would go negative.

All operations stay `O(length)`.
""",
    "design-add-and-search-words-data-structure": """
A plain trie, with the wildcard handled during the search rather than the insert.

On a letter, follow that single edge. On a `'.'`, recurse into **every** child — that branching is
the entire cost of the feature.

Adding is `O(length)`. Searching is `O(length)` with no wildcards and up to `O(26^dots * length)`
with them, which is why the dot count is capped.
""",
    "longest-string-with-all-prefixes": """
Insert everything into a trie, then walk down only through nodes that mark the end of a word — that
condition is exactly "every prefix is also present".

Visiting children in alphabetical order makes the lexicographic tie-break fall out for free: the
first longest path found is the smallest one.

`O(total characters)` time and space.
""",
    "number-of-distinct-substrings": """
Every substring is a prefix of some suffix, so insert all `n` suffixes into a trie. Each **new node**
created is one distinct substring — no need to store the substrings themselves.

`O(n^2)` time and nodes, which is fine at this size. A suffix automaton or suffix array with LCP
gets it to `O(n)` or `O(n log n)` for much longer strings.
""",
    "maximum-xor-of-two-numbers-in-an-array": """
Checking every pair is `O(n^2)`. Both standard answers build the answer bit by bit from the top.

The trie version stores the numbers as 32-bit paths and, for each value, walks preferring the
opposite bit at every level — greedily grabbing the highest bits.

The prefix-set version does the same without a trie: assume the next bit of the answer is `1`, and
check whether two masked prefixes XOR to that candidate. Both are `O(32 n)`.
""",
    "maximum-xor-with-an-element-from-array": """
Each query restricts which elements may be used, so the trie cannot simply hold everything.

Process the queries **offline**: sort the numbers ascending and the queries by their limit, then
insert numbers into the trie as the limit grows. When a query is handled, the trie contains exactly
the elements it is allowed to use.

`O((n + q) log n)` for the sorts plus `O(32(n + q))` for the trie work. An empty trie means `-1`.
""",
    "reverse-words-in-a-string": """
Splitting on whitespace, dropping empty pieces, reversing and joining is the honest one-liner in most
languages, and it is `O(n)`.

The in-place version — reverse the whole string, then reverse each word — is the interview answer
for languages with mutable strings and `O(1)` extra space. Multiple, leading and trailing spaces are
what the test cases are really probing.
""",
    "compare-version-numbers": """
Split on dots and compare part by part as integers, which handles leading zeros for free.

The subtle rule is the missing parts: `1.0` equals `1`, so iterate to the longer of the two lengths
and treat anything past the end as `0`.

`O(n + m)` time, `O(1)` space if the parts are parsed on the fly rather than split up front.
""",
    "rabin-karp": """
Hash the pattern once, then slide a window over the text updating its hash in `O(1)`: subtract the
leading character's contribution, multiply by the base, add the new character.

Always verify a hash match character by character — different strings can hash the same, and a
version that skips the check is not a correct algorithm, just a fast one that is usually right.

`O(n + m)` expected, `O(n * m)` in a pathological worst case.
""",
    "z-algorithm": """
`z[i]` is the length of the longest substring starting at `i` that matches a prefix of the string.

The trick is reusing work: keep the rightmost matching segment `[l, r]` seen so far. Inside that
segment, `z[i]` can be seeded from `z[i - l]` because that stretch is known to match, and only the
part beyond `r` needs real comparisons.

Each comparison either extends `r` or ends an entry, so the total is `O(n)`.
""",
    "kmp-algorithm": """
The failure function stores, for each prefix of the pattern, the length of its longest proper prefix
that is also a suffix.

On a mismatch, that table says how far the pattern can slide without missing an occurrence, so the
text pointer never moves backwards. On a full match, falling back through the table is what allows
overlapping matches.

Building the table is `O(m)`, scanning is `O(n)`.
""",
    "encode-and-decode-strings": """
Any separator can appear inside the payload, so no delimiter alone is safe. Length-prefixing is:
write `len(word)` then a marker then the word itself.

The decoder reads digits up to the marker, then takes exactly that many characters — the content is
never scanned for structure, so `"3#abc"` inside a string is harmless.

`O(total characters)` both ways, and it handles empty strings without a special case.
""",
})
