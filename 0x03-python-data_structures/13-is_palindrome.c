#include "lists.h"
int is_palindrome(listint_t **head)
{
listint_t *fast_ptr, *first_half, *second_half;
listint_t *slow_ptr, *tmp;
int result = 0;
if (head == NULL)
return (0);
first_half = fast_ptr = tmp = slow_ptr = *head;
second_half = NULL;
if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
tmp = slow_ptr;
slow_ptr = slow_ptr->next;
}
if (fast_ptr != NULL)
{
tmp = slow_ptr;
slow_ptr = slow_ptr->next;
}
second_half = slow_ptr;
reverse_linked_list(&second_half);
result = list_compare(first_half, second_half);
reverse_linked_list(&second_half);
tmp->next = second_half;
return (result);
}

void reverse_linked_list(listint_t **head)
{
listint_t *tmp, *prev, *current;
prev = NULL;
current = tmp = *head;
while (tmp)
{
tmp = current->next;
current->next = prev;
prev = current;
current = tmp;
}
*head = prev;
}

int list_compare(listint_t *list1, listint_t *list2)
{
while (list2 != NULL)
{
if (list1->n != list2->n)
{
return (0);
}
list1 = list1->next;
list2 = list2->next;
}
return (1);
}
