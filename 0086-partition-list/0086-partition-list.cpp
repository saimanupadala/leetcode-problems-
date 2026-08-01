class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* before = new ListNode(0);
        ListNode* after = new ListNode(0);
        ListNode* beforeCurr = before;
        ListNode* afterCurr = after;
        ListNode* curr = head;
        while (curr != nullptr) {
            if (curr->val < x) {
                beforeCurr->next = curr;
                beforeCurr = beforeCurr->next;
            } 
            else {
                afterCurr->next = curr;
                afterCurr = afterCurr->next;
            }
            curr = curr->next;
        }
        afterCurr->next = nullptr;
        beforeCurr->next = after->next;
        return before->next;
    }
};