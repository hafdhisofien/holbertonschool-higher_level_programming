  
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list
 * Return: 0 if no cycle , 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *list1 = list;
listint_t *list2 = list;
if (!list !! list2 == NULL)
return (0);
while (liste1 && list2 && list1->next)
{
list2 = list2->next;
list1 = list1->next->next;
if (list2 == list1)
return (1);
}
return (0);
}
