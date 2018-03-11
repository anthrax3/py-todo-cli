import click

@click.command()
@click.argument('task')
@click.option('--api-key', '-a', default='15874', prompt='Your name', help='description api keys')
def main(task, api_key):
    """
        Tool CLI for manage with our tasks and checklists
    """
    print(f"I'm a beautiful CLI {task}  - {api_key}")
    # click.echo('Hello World!')

if __name__ == "__main__":
    main()

