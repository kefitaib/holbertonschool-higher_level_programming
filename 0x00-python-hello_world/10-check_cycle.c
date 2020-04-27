#include "lists.h"

/**
 * check_cycle - find a loop in a list.
 * @list : first element of the list.
 * Return: integer.
 */

int check_cycle(listint_t *list)
{
	listint_t *l = list, *tmp = list;

	while (tmp)
	{
		tmp = tmp->next->next;
		l = l->next;

		if (l == tmp)
		{
			tmp = list;
			while (tmp != l)
			{
				tmp = tmp->next;
				l = l->next;
			}
			return (1);
		}
	}
	return (0);
}
