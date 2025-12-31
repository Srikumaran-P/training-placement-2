var deleteDuplicates = function (head) {
    if (!head || !head.next) return head;

    if (head.val === head.next.val) {
        let curr = head.next;
        while (curr && curr.val === head.val) {
            curr = curr.next;
        }
        return deleteDuplicates(curr)
    } else {
        head.next = deleteDuplicates(head.next);
        return head;
    }
};
