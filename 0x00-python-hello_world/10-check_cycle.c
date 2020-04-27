#include "lists.h"

/**
 * check_cycle - find a loop in a list.
 * @list : first element of the list.
 * Return: integer.
 */

int check_cycle(listint_t *list)
{
	listint_t *l = NULL, *tmp = NULL;

	if (!list || !(list->next))
		return (0);

	tmp = list->next->next;
	l = list;
	while (tmp)
	{
		if (l == tmp)
			return (1);
		tmp = tmp->next->next;
		l = l->next;
	}
	return (0);
}
