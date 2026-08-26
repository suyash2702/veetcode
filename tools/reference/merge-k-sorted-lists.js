var mergeKLists = function (lists) {
  const values = [];
  for (const head of lists) {
    for (let node = head; node; node = node.next) values.push(node.val);
  }
  values.sort((a, b) => a - b);
  let head = null;
  for (let i = values.length - 1; i >= 0; i--) head = new ListNode(values[i], head);
  return head;
};
