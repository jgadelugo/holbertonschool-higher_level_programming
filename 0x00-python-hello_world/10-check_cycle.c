#include "lists.h"

/**
 * check_cycle - finds a loop in a linked list
 * @list: beggining of linked list
 * Return: 1 if loop 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	while (list && (*list).next)
	{
		slow = list;
		fast = (*list).next;
		while (slow != fast)
		{
			if (slow)
				slow = (*slow).next;
			if (fast == list)
				return (1);
			if (fast)
				fast = (*fast).next;
			if (fast == list)
				return (1);
			if (fast)
				fast = (*fast).next;
			if (fast == list)
				return (1);
		}
		list = (*list).next;
	}
	return (0);
}
