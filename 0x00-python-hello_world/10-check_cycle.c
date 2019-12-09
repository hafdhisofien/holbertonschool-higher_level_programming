#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @head: pointer to list to be freed
 * Return: 0 if has no cycle or 1 if has cycle
 */
int check_cycle(listint_t *list)
{
listint_t *list1 = list;
listint_t *list2 = list;
if (!list || list->next == NULL)
return (0);
while (list1 && list2 && list2->next && list1->next->next)
{
list1 = list1->next;
list2 = list2->next->next;
if (list1 == list2)
return (1);
}
return (0);
}
