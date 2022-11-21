import asyncio

def sync_a():
    print('동기 함수')

async def sync_b():
    print('비동기 함수')

#실행방법 1. 다른 비동기 함수 내에서 호출
async def sync_main():
    sync_a()

#파이썬 버전 3.7 이상의 경우
asyncio.run(sync_main())



def deco(func):
    def decorated():
        print('a')
        func()
        print('b')
    return decorated

@deco
def main1():
    print('메인 1 함수입니다.')

@deco
def main2():
    print('메인 2 함수입니다.')

main1()
main2()