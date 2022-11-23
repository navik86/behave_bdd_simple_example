from behave import *

import projects.check_relation_people as crp


@given("collect couples of people in container")
def step(context):
    context.container = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )


@when("create net of people")
def step(context):
    context.net = crp.create_net(context.container)


@then('check relation "{first_people}" and "{second_people}"')
def step(context, first_people, second_people):
    assert crp.check_relation(context.net, first_people, second_people) is True
