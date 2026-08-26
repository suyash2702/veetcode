var longestPalindrome = function (s) {
  let best = '';
  const grow = (lo, hi) => {
    while (lo >= 0 && hi < s.length && s[lo] === s[hi]) {
      lo--;
      hi++;
    }
    const candidate = s.slice(lo + 1, hi);
    if (candidate.length > best.length) best = candidate;
  };
  for (let i = 0; i < s.length; i++) {
    grow(i, i);
    grow(i, i + 1);
  }
  return best;
};
