test = {
  'name': 'tally',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (assert-equal '((obama . 1)) '(tally '(obama)))
          ok
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (assert-equal '((taft . 3)) '(tally '(taft taft taft)))
          ok
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (assert-equal '((jerry . 2) (brown . 1)) '(tally '(jerry jerry brown)))
          ok
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (assert-equal '((jane . 5) (jack . 2) (jill . 1)) '(tally '(jane jack jane jane jack jill jane jane)))
          ok
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (assert-equal '((jane . 5) (jack . 2) (jill . 1)) '(tally '(jane jack jane jane jill jane jane jack)))
          ok
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab14)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
