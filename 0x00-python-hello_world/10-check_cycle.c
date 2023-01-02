#include "lists.h"
/**
 * check_cycle - find loop start
 * @list: pointer to head pointer of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *fast, *slow;
fast = slow = list;
while (slow && fast && fast->next)
{
fast = fast->next->next;
slow = slow->next;
if (slow == fast)
{
return (1);
}
}
return (0);
}
