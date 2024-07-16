def show_args(*args):
    '''与えられた複数の位置引数をタプルにまとめて受け取りそのタプルを表示して返す'''
    print('positional arguments:', args)
    return args

def show_kwargs(**kwargs):
    '''与えられた複数のキーワードを辞書にまとめて受け取りその辞書を表示して返す'''
    print('Keyword arguments:', kwargs)
    return kwargs
        
