#include "lists.h"
/**
 * insert_node - add nodes at some place.
 * @head: the head of the linked list
 * @number: the n value of the node
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
	}
	else if (number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && current->next->n < number)
		{
		current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}

