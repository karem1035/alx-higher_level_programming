#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in the linked list
 * @list: The list to be checked
 * Return: 1 if the is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
