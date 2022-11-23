Feature: check relation

  Scenario: check relation
     Given collect couples of people in container
      When create net of people
      Then check relation "Маша" and "Петя"