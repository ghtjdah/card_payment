from iamport import Iamport

#-------------사용하기 위한 객체 만들기-------------#
def makeimaport():
    # 상점정보?
    iamport = Iamport(imp_key='4463657570405001',
                      imp_secret='o6Ntie0KDH6fcTOXUh2tj4ELwyFmsq3QwRjP6jzJ0GZdANau5dYohDaOcQbEgeuN6NCc7cW8SVltJwXP')
    return iamport


#----------------결제 정보 찾기----------------#
def findpayment(iamport, impuid):
    # 상품 아이디로 확인
    # response = iamport.find(merchant_uid='{상품 아이디}')
    # I'mport 아이디로 확인
    response = iamport.find(imp_uid=impuid)
    # print(response)
    return response


#----------------결제 가격 확인----------------#
def checkpayment(iamport, response):
    # 상품 아이디로 확인
    # iamport.is_paid(5000, merchant_uid='{상품 아이디}')
    # I'mport 아이디로 확인
    result = iamport.is_paid(1000, imp_uid='imp_239417088182')
    # 이미 찾은 response 재활용하여 확인
    # iamport.is_paid(5000, response=response)
    return  result


#---------------------결제 취소---------------------#
def cancelpayment(iamport):
    # 상품 아이디로 취소
    # response = iamport.cancel(u'취소하는 이유', merchant_uid='{상품 아이디}')
    # I'mport; 아이디로 취소
    # response = iamport.cancel(u'취소하는 이유', imp_uid='imp_239417088182')

    # 취소시 오류 예외처리(이미 취소된 결제는 에러가 발생함)
    try:
        response = iamport.cancel(u'취소 테스트', imp_uid='imp_239417088182')
    except Iamport.ResponseError as e:
        print(e.code)
        print(e.message)  # 에러난 이유를 알 수 있음
    except Iamport.HttpError as http_error:
        print(http_error.code)
        print(http_error.reason) # HTTP not 200 에러난 이유를 알 수 있음
    else:
        return response


#------------------1회성 비인증 결제------------------#
def unsignedpay(iamport):
    # 테스트용 값
    payload = {
        'merchant_uid': 'merchant_1231231231235',
        'amount': 1000,
        'card_number': '5272-8999-8547-8143',
        'expiry': '2022-04',
        'birth': '950104',
        'pwd_2digit': '25'
    }
    try:
        response = iamport.pay_onetime(**payload)
    except KeyError as e:
        # 필수 값이 없을때 에러 처리
        assert "Essential parameter is missing!: card_number" in str(e)
    except Iamport.ResponseError as e:
        # 응답 에러 처리
        assert e.code == -1
        assert u'카드정보 인증에 실패하였습니다.' in e.message
    except Iamport.HttpError as http_error:
        # HTTP not 200 응답 에러 처리
        pass
    else:
        return response


#--------------------재결제--------------------#
def payagain(iamport):
    # 테스트용 값
    payload = {
        'customer_uid': 'StdpayISP_INIpayTest20181127110753801091',
        'merchant_uid': 'merchant_1543285806645',
        'amount': 1000,
    }
    try:
        response = iamport.pay_again(**payload)
    except KeyError:
        # 필수 값이 없을때 에러 처리
        pass
    except Iamport.ResponseError as e:
        # 응답 에러 처리
        print(e)
    except Iamport.HttpError as http_error:
        # HTTP not 200 응답 에러 처리
        pass
    else:
        return response


#------------------결제될 내역 사전정보 등록------------------#
def registerpayinform(iamport):
    # 테스트용 값
    amount = 12000
    mid = 'merchant_test'
    try:
        response = iamport.prepare(amount=amount, merchant_uid=mid)
    except Iamport.ResponseError as e:
        # 응답 에러 처리
        pass
    except Iamport.HttpError as http_error:
        # HTTP not 200 응답 에러 처리
        pass


#------------------결제될 내역 사전정보 확인------------------#
def confirmpayinform(iamport):
    # 테스트용 값
    amount = 12000
    mid = 'merchant_test'
    try:
        result = iamport.prepare_validate(merchant_uid=mid, amount=amount)
    except Iamport.ResponseError as e:
        # 응답 에러 처리
        pass
    except Iamport.HttpError as http_error:
        # HTTP not 200 응답 에러 처리
        pass


if(__name__ == '__main__'):
    iamport = makeimaport()
    result = findpayment(iamport, 'imp_239417088182')
    # result = checkpayment(iamport, response)
    # result = cancelpayment(iamport)
    # result = payagain(iamport)

    print(result)
    # print(result.get[''])
