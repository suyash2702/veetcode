var groupAnagrams = function (strs) {
  const buckets = new Map();
  for (const word of strs) {
    const key = [...word].sort().join('');
    if (!buckets.has(key)) buckets.set(key, []);
    buckets.get(key).push(word);
  }
  return [...buckets.values()];
};
