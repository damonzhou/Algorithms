#include <iostream>
#include <vector>
#include <unordered_map>


/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* initList(std::vector<int> v) {
        ListNode *l = NULL, *prev;
        for (int i = 0; i < v.size(); i++) {
            ListNode *tmp = new ListNode(v[i]);
            if (l == NULL) {
                l = tmp;
                prev = l;
            } else {
                prev->next = tmp;
            }
            prev = tmp;
        }

        return l;
    }

    void releaseList(ListNode *l) {
        ListNode *tmp = l;
        ListNode *next;
        for (tmp = l; tmp != NULL;) {
            next = tmp->next;
            if (tmp) {
                // std::cout << tmp->val << std::endl;
                delete tmp;
            }
            tmp = next;
        }
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        struct ListNode *l3 = NULL;
        struct ListNode *prev = l3, *p = l1, *q = l2;
        int carrier = 0;

        while (p || q || carrier) {
            struct ListNode *tmp = new ListNode(0);
            if (l3 == NULL) {
                l3 = tmp;
                prev = tmp;
            } else {
                prev->next = tmp;
            }

            int v1 = 0, v2 = 0;
            if (p) {
                v1 = p->val;
                p = p->next;
            }
            if (q) {
                v2 = q->val;
                q = q->next;
            }

            int v3 = v1 + v2 + carrier;
            if (v3 > 9) {
                v3 -= 10;
                carrier = 1;
            } else {
                carrier = 0;
            }
            tmp->val = v3;

            prev = tmp;
        }

        return l3;
    }

    ListNode * reverseList(ListNode *l) {
        ListNode * head = NULL;
        ListNode *next;
        for (ListNode *v = l; v != NULL;) {
            next = v->next;
            if (head == NULL) {
                head = v;
                head->next = NULL;
            } else {
                v->next = head;
                head = v;
            }

            v = next;
        }

        return head;
    }

    void printList(ListNode *l) {
        ListNode * newList = reverseList(l);
        for (ListNode *v = newList; v != NULL; v = v->next)
        {
            std::cout << v->val;
        }
        std::cout << std::endl;
    }

};



int main()
{
    const int num1[] = {5, 7};
    const int num2[] = {6, 2, 3};
    std::vector<int> num1_vec(num1, num1 + sizeof(num1) / sizeof(int));
    std::vector<int> num2_vec(num2, num2 + sizeof(num2) / sizeof(int));
    Solution *s = new Solution();
    ListNode *l1 = s->initList(num1_vec);
    ListNode *l2 = s->initList(num2_vec);
    ListNode *l3 = s->addTwoNumbers(l1, l2);
    s->printList(l1);
    s->printList(l2);
    s->printList(l3);
    s->releaseList(l1);
    s->releaseList(l2);
    s->releaseList(l3);
    return 0;
}
