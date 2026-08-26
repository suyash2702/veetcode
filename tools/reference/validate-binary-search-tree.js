// Exercises the LeetCode-style `class Solution` shape.
class Solution {
  isValidBST(root) {
    const walk = (node, low, high) => {
      if (!node) return true;
      if (node.val <= low || node.val >= high) return false;
      return walk(node.left, low, node.val) && walk(node.right, node.val, high);
    };
    return walk(root, -Infinity, Infinity);
  }
}
