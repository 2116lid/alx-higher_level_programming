#include "lists.h"

/**
 * check_cycle - a function to check if a linked list contains a cycle
 * @list: the linked list to check.
 *
 * Return: 1 if the list has a cycle, 0 on failure.
 */
int check_cycle(listint_t *list)
{
	listint_t *pac = list;
	listint_t *pace = list;

	if (!list)
		return (0);

	while (pac != NULL && pace != NULL && pace->next != NULL)
	{
		pac = pac->next;
		pace = pace->next->next;

		if (pac == pace)
			return (1);
	}
	return (0);
}
