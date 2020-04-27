#include "lists.h"

/**
 * check_cycle - find a loop in a list.
 * @list : first element of the list.
 * Return: integer.
 */

int check_cycle(listint_t *list)
{
	listint_t *l = list, *tmp = list;

	if (!list || !(list->next))
		return (0);

	while (tmp->next && tmp)
	{
		tmp = tmp->next->next;
		l = l->next;
		if (l == tmp)
			return (1);
	}
	return (0);
}
