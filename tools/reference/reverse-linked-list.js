// Exercises module.exports resolution as well as ListNode marshalling.
function reverseList(head) {
  let prev = null;
  while (head) {
    const next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }
  return prev;
}
module.exports = { reverseList };
