test = {
  'name': 'foldr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (foldr (lambda (x y) (+ x y)) 0 '(1 2 3))
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (foldr (lambda (x y) (* x y)) 1 '(1 2 3))
          6
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
