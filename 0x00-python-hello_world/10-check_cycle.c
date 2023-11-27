#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list : pointer to head of the list
  * Return: 1 (loop), 0 (not loop)
  */

int check_cycle(listint_t *list)
{
	listint_t *cat = list;
	listint_t *dog = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (dog != NULL && cat != NULL && cat->next->next && dog->next)
	{
		dog = dog->next->next;
		cat = cat->next;
		if (cat == dog)
		return (1);
	}
return (0);
}
