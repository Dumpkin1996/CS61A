test = {
  'name': 'map',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (map '(1 2 3) (lambda (x) (* x x)))
          (1 4 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (map '(6 1) (lambda (x) (+ x 1)))
          (7 2)
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
