from minitools.github.blog import BlogManager, GatherManager

if __name__ == '__main__':
    # BlogManager(__file__).create()
    # GatherManager(__file__, absolute='http://127.0.0.1:8866/api/blog?filePath=.').gather()
    GatherManager(__file__, absolute='https://czaorz.github.io/Articles').gather()
