from forgecore.cli import DjangoClickAliasCommand

from forgeheroku.cli import cli


class Command(DjangoClickAliasCommand):
    click_command = cli
