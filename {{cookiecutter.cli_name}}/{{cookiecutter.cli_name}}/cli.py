import click


import logging
import logging.config

logger = logging.getLogger(__name__)

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


@click.group()
@click.pass_context
@click.option("--debug/--no-debug", default=False)
@click.option("--config", default="config.ini")
@click.option("--env", default="dev")
def cli(ctx, debug, config, env):
    ctx.ensure_object(dict)
    cfg.load(config, env)
    # if debug:
    #     logging.basicConfig(level=logging.DEBUG)
    # else:
    #     logging.basicConfig(level=logging.INFO)
    ctx.obj['STATS_ENV']=env


@cli.command("hello")
@click.pass_context
@click.option("--name", default="Howdy")
def weeklycollect(name):
    click.echo(f'Hello {name}!')

if __name__ == "__main__":
    logger.info("starting to run")
    cli()
