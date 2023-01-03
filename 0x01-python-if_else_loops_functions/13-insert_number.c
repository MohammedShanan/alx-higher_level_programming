#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node, *tmp;
node = malloc(sizeof(listint_t));
if (node == NULL)
{
return (NULL);
}
node->n = number;
tmp = *head;
while (tmp)
{
if (tmp->next)
{
if (tmp->next->n >= number && tmp->n <= number)
{
node->next = tmp->next;
tmp->next = node;
return (node);
}
else if (tmp->n >= number)
{
node->next = tmp;
*head = node;
return (node);
}
}
else
{
tmp->next = node;
node->next = NULL;
return (node);
}
tmp = tmp->next;
}
*head = node;
node->next = NULL;
return (node);
}
