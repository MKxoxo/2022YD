{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "python0424.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOyThiLtyIi65OZ+2RnVHQ3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MKxoxo/2022YD/blob/main/python0424.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###DAY1\n",
        "\n"
      ],
      "metadata": {
        "id": "YCRASP7fDyCW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#001 print 기초\n",
        "#화면에 Hello World 문자열을 출력하세요.\n",
        "s = 'Hello World'\n",
        "print(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3vQO3WHK4T9T",
        "outputId": "ccd71c3f-6ed6-42c6-d9e9-8ced795d47af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#002 print 기초\n",
        "#화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)\n",
        "print(\"Mary's cosmetics\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0C9CcwqA4bP9",
        "outputId": "4ea14bdd-ce90-4ed3-9ee0-e11821e1366c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mary's cosmetics\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#003 화면에 아래 문장을 출력하세요. (중간에 \"가 있음에 주의하세요.)\n",
        "#신씨가 소리질렀다. \"도둑이야\".\n",
        "print('신씨가 소리질렀다. \"도둑이야.\"')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZOe7afO04lpy",
        "outputId": "2a947518-4480-4686-fe11-e4ddd3b86eb0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "신씨가 소리질렀다. \"도둑이야.\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#004 화면에 \"C:\\Windows\"를 출력하세요.\n",
        "s = \"C:\\Windows\"\n",
        "print(f'\"{s}\"')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1nIOuSfg5KIq",
        "outputId": "3c86557e-e30b-4770-9de4-3933d06f2a4e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\"C:\\Windows\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#005 다음 코드를 실행해보고 \\t와 \\n의 역할을 설명해보세요.\n",
        "\n",
        "print(\"안녕하세요.\\n만나서\\t\\t반갑습니다.\")\n",
        "\n",
        "# \\n (줄바꿈)\n",
        "# \\t (tab key)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "skMn3WBi5uoJ",
        "outputId": "89895b89-5b34-453a-e2c8-41ef14b91267"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "안녕하세요.\n",
            "만나서\t\t반갑습니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 006 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.\n",
        "print(\"오늘은\", \"일요일\") \n",
        "#오늘은 띄고 일요일 둘 다 출력됨"
      ],
      "metadata": {
        "id": "UC7HQsYr6CbC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#007 print() 함수를 사용하여 다음과 같이 출력하세요.\n",
        "#naver;kakao;sk;samsung\n",
        "print('naver;kakao;sk;samsung')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AGo_5t056iKl",
        "outputId": "c5b228bf-0827-44fb-b798-262474934ea5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "naver;kakao;sk;samsung\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#008 print() 함수를 사용하여 다음과 같이 출력하세요.\n",
        "#naver/kakao/sk/samsung\n",
        "print('naver','kakao','sk','samsung', sep='/')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tCvREHwf7Fn-",
        "outputId": "6025d032-1efa-416b-e43a-660d855c0b92"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "naver/kakao/sk/samsung\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 009 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.\n",
        "#print(\"first\");print(\"second\") \n",
        "\n",
        "print(\"first\",end='');print(\"second\") "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SiRAaApW7Ys4",
        "outputId": "6b11735f-4c0f-4957-8f57-73b401c9ce8f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "firstsecond\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 010 연산 결과 출력 5/3의 결과를 화면에 출력하세요.\n",
        "a = 5\n",
        "b = 3\n",
        "print(a/b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cpq2PI1S8LkO",
        "outputId": "4d1f98ea-373e-409f-8af8-0b094b61dd8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.6666666666666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#011 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.\n",
        "삼성전자 = 50000\n",
        "총평가금액 = 삼성전자 * 10\n",
        "print(총평가금액)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DnSluG4C8YI9",
        "outputId": "f6e0bf64-59e3-4718-bd63-d352f7b8fbce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "500000"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#012 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.\n",
        "#항목 값 \n",
        "#시가총액 298조 \n",
        "#현재가 50,000원 \n",
        "#PER 15.79\n",
        "시가총액 = '298조'\n",
        "현재가 = 50000\n",
        "per = 15.78\n",
        "print(시가총액, 현재가, per)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rBTH6UPM90BP",
        "outputId": "54076888-d19d-453b-d60b-4b533de903ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "298조 50000 15.78\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#013 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.\n",
        "#s = \"hello\" t = \"python\" 두 변수를 이용하여 아래와 같이 출력해보세요. 실행 예: hello! python\n",
        "s = \"hello\"\n",
        "t = \"python\"\n",
        "print(s+'!',t)"
      ],
      "metadata": {
        "id": "9UZk3TUJ-QyO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8d360653-fb2f-4203-9d61-e54ab5a981a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello! python\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#014 아래 코드의 실행 결과를 예상해보세요.\n",
        "#2 + 2 * 3 \n",
        "\n",
        "#2*3이 된 다음 +2가 됨 답  8"
      ],
      "metadata": {
        "id": "Iwj9AGyotIP2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#015 type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.\n",
        "#a = 128 print (type(a)) <class 'int'> 아래 변수에 바인딩된 값의 타입을 판별해보세요.\n",
        "a = \"132\"\n",
        "type(a)\n",
        "#타입은 str - 문자열"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cYBb9wNftQcM",
        "outputId": "a8e615cc-ef09-4ed6-cbcb-8f3519ffc892"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#016 문자열 '720'를 정수형으로 변환해보세요.\n",
        "#num_str = \"720\"\n",
        "\n",
        "num_str = \"720\"\n",
        "num_int = int(num_str)\n",
        "print(num_int , type(num_int))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Oc0acGgwtRaw",
        "outputId": "6562455f-4211-494e-bcbc-271140db5c1b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "720 <class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#017 정수 100을 문자열 '100'으로 변환해보세요.\n",
        "#num = 100\n",
        "num = 100\n",
        "mz = str(num)\n",
        "print(mz, type(mz))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vzLkzz6YtVtv",
        "outputId": "3c811604-493b-4f2c-de70-029d36b84594"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#018 문자열 \"15.79\"를 실수(float) 타입으로 변환해보세요.\n",
        "s = float(\"15.79\")\n",
        "print(s,type(s))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xMsnjaYMtfVm",
        "outputId": "3b8e43ca-f6fc-4c31-c6d8-063cafd4bd47"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15.79 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 019 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.\n",
        "year = \"2020\"\n",
        "#print(year)\n",
        "yr_i = int(year)\n",
        "for i in range(1,4):\n",
        "   print(yr_i - i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "73jxK0awtfL7",
        "outputId": "6526b5a9-7271-44f8-c289-19356e88b4e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2019\n",
            "2018\n",
            "2017\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#020 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)\n",
        "\n",
        "mon_aircon = 48584\n",
        "total_price = mon_aircon * 36\n",
        "print(total_price)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g6XSLTAMtfEQ",
        "outputId": "ce49c9be-a860-4da5-989e-25d9c66fdc87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1749024\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#021 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요. >> letters = 'python' / 실행 예 p t\n",
        "letters = 'python'\n",
        "print(letters[:3].replace('y',' '))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1jZ3KTs6-TLB",
        "outputId": "0799ae1c-ee67-49ce-f307-f3a14a446438"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "p t\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#022 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요. >> license_plate = \"24가 2210\" / 실행 예: 2210\n",
        "license_plate = \"24가 2210\"\n",
        "print(license_plate[4:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9SeMUkIX-THp",
        "outputId": "041cf6fa-a3cf-4b32-e3d5-5e1bf4647c51"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2210\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#023 아래의 문자열에서 '홀' 만 출력하세요. >> string = \"홀짝홀짝홀짝\" 실행 예: 홀홀홀\n",
        "string = \"홀짝홀짝홀짝\"\n",
        "print(string.replace('짝',''))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CJgWQXfo-TDt",
        "outputId": "b5dce6bb-e661-43f7-b9c0-a7868afd2990"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "홀홀홀\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#024 문자열을 거꾸로 뒤집어 출력하세요. >> string = \"PYTHON\" 실행 예: NOHTYP\n",
        "string = \"PYTHON\"\n",
        "print(string[::-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C3q0fj1i-TAl",
        "outputId": "a11dd937-5c89-4092-a219-a7dafc19944c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NOHTYP\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#025 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요. >> phone_number = \"010-1111-2222\" 실행 예 010 1111 2222\n",
        "phone_number = \"010-1111-2222\"\n",
        "phn_nm = phone_number.replace('-',' ')\n",
        "print(phn_nm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9ChTnYpm-S8t",
        "outputId": "760376c8-c160-4fb4-dd73-c3ebb76cd6f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "010 1111 2222\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#026 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요. 실행 예 01011112222\n",
        "\n",
        "print(phn_nm.replace(' ',''))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Sv0KcLj-S1d",
        "outputId": "d9769086-91b7-48e5-f25f-0a30b418f2f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "01011112222\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#027 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요. >> url = \"http://sharebook.kr\" 실행 예: kr\n",
        "url = \"http://sharebook.kr\"\n",
        "print(url[-2:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iyYACu0O-Sws",
        "outputId": "0698151e-aa37-4cc9-d61b-6ee57cf0f299"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "kr\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#028 문자열은 immutable 아래 코드의 실행 결과를 예상해보세요.\n",
        "\n",
        "#>> lang = 'python'\n",
        "#>> lang[0] = 'P'\n",
        "#>> print(lang)\n",
        "\n",
        "print(\"'python'이 출력됩니다. 문자열은 immutable 수정될 수 없음\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DX4Mb98eDIqj",
        "outputId": "6a6e318a-2e4d-4d36-bc42-33ca5b86c3be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "'python'이 출력됩니다. 문자열은 immutable 수정될 수 없음\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#029 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요. >> string = 'abcdfe2a354a32a' 실행 예: Abcdfe2A354A32A\n",
        "string = 'abcdfe2a354a32a'\n",
        "print(string.replace('a','A'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1YNSoTLcDNys",
        "outputId": "6a55117c-e018-4363-ada4-7a3791dfb8cd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Abcdfe2A354A32A\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#030 아래 코드의 실행 결과를 예상해보세요. >> string = 'abcd' >> string.replace('b', 'B') >> print(string)\n",
        "print(\"string의 소문자 b 가 대문자 B가 됨\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Qz8BEnuDRZF",
        "outputId": "39b0b96e-c398-4f4e-94c3-2416eaf9618c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "string의 소문자 b 가 대문자 B가 됨\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#031 아래 코드의 실행 결과를 예상해보세요.\n",
        "\n",
        "#>> a = \"3\"\n",
        "#>> b = \"4\"\n",
        "#>> print(a + b)\n",
        "\n",
        "print('공백없이 ab가 합쳐져 \"34\"가 출력')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZOpSwZIsJCG-",
        "outputId": "e3a33280-2ab3-45b2-bcda-37fd80143ef5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "공백없이 ab가 합쳐져 \"34\"가 출력\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#032 아래 코드의 실행 결과를 예상해보세요.\n",
        "\n",
        "#>>print(\"Hi\" * 3)\n",
        "print('HiHiHi')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EZSZkpm2JCBA",
        "outputId": "6e800d3a-8670-4bb8-c4cb-5cc35f9df909"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HiHiHi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#033 화면에 '-'를 80개 출력하세요.\n",
        "#실행 예:--------------------------------------------------------------------------------\n",
        "a = '-'\n",
        "print(a*80)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SwGZIi56JB7w",
        "outputId": "42819e73-8cb9-4f3f-a4e2-05dd9a5fe5ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--------------------------------------------------------------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#034 변수에 다음과 같은 문자열이 바인딩되어 있습니다.\n",
        "t1 = 'python'\n",
        "t2 = 'java'\n",
        "\n",
        "#변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.\n",
        "#실행 예:python java python java python java python java\n",
        "\n",
        "print((t1+' '+t2+' ')*4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NRhwIEuHJB1x",
        "outputId": "29eecb1d-55b5-4700-9a08-ff4b7c0f70cc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "python java python java python java python java \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#035 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.\n",
        "\n",
        "name1 = \"김민수\" \n",
        "age1 = 10\n",
        "name2 = \"이철희\"\n",
        "age2 = 13\n",
        "print('이름: %s 나이: %d'%(name1,age1))\n",
        "print('이름: %s 나이: %d'%(name2,age2))\n",
        "#이름: 김민수 나이: 10\n",
        "#이름: 이철희 나이: 13"
      ],
      "metadata": {
        "id": "wZuT7PzaJBwU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "851ffe41-9ca1-43ba-f3fb-05911b374189"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "이름: 김민수 나이: 10\n",
            "이름: 이철희 나이: 13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#036 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.\n",
        "name1 = \"김민수\" \n",
        "age1 = 10\n",
        "name2 = \"이철희\"\n",
        "age2 = 13\n",
        "print('이름: {} 나이: {}'.format(name1,age1))\n",
        "print('이름: {} 나이: {}'.format(name2,age2))"
      ],
      "metadata": {
        "id": "xcCRbZz_JBr5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c9b7020e-a6bb-41a1-8f0a-3dfc407ab0f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "이름: 김민수 나이: 10\n",
            "이름: 이철희 나이: 13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#037 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.\n",
        "\n",
        "name1 = \"김민수\" \n",
        "age1 = 10\n",
        "name2 = \"이철희\"\n",
        "age2 = 13\n",
        "print(f'이름: {name1} 나이: {age1}')\n",
        "print(f'이름: {name2} 나이: {age2}')"
      ],
      "metadata": {
        "id": "6czPRUURJBne",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "531bbd9f-21d4-4aa3-8873-0796a06620d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "이름: 김민수 나이: 10\n",
            "이름: 이철희 나이: 13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#038 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.\n",
        "\n",
        "상장주식수 = \"5,969,782,550\"\n",
        "int_stk = 상장주식수.replace(',','')\n",
        "상장주식수i = int(int_stk)\n",
        "print(상장주식수i,type(상장주식수i))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TO5WOfQ4JBjU",
        "outputId": "3c7bc072-6d6e-47f9-f667-10ae59eb75c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5969782550 <class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#039 다음과 같은 문자열에서 '2020/03'만 출력하세요.\n",
        "\n",
        "분기 = \"2020/03(E) (IFRS연결)\"\n",
        "날짜 = 분기[:7]\n",
        "print(날짜)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WE7dTq_XJBd8",
        "outputId": "9190ce8e-2cdf-42c9-843b-1d6c72dc848c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2020/03\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#040 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.\n",
        "\n",
        "data = \"   삼성전자    \"\n",
        "print(data.strip())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e0itgVKaKt3k",
        "outputId": "001bf8b6-707e-460b-a646-4ee069be92f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "삼성전자\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#041 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.\n",
        "\n",
        "ticker = \"btc_krw\"\n",
        "\n",
        "print(ticker.upper())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L2yAFKD3OUp7",
        "outputId": "11205c1e-0a14-4c4f-9460-72fd9186df00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "BTC_KRW\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#042 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.\n",
        "\n",
        "ticker = \"BTC_KRW\"\n",
        "\n",
        "print(ticker.lower())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DUBVt9SfShRI",
        "outputId": "31019cfb-dfa1-40c3-aa00-7f62b223f6de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "btc_krw\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#043 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.\n",
        "\n",
        "s = 'hello'\n",
        "s.capitalize()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "9LxHYLivSkas",
        "outputId": "85528101-3e86-4cbb-d041-676560220382"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Hello'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 142
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#044 endswith 메서드\n",
        "#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.\n",
        "\n",
        "file_name = \"보고서.xlsx\"\n",
        "\n",
        "if file_name.endswith('xlsx') == True :\n",
        "  print(True or False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RMIpe2a8Sm62",
        "outputId": "701bde53-ffe5-4b2b-a45e-cb804b90c60f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#045 endswith 메서드\n",
        "#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.\n",
        "\n",
        "file_name = \"보고서.xlsx\"\n",
        "file_name.endswith(('xlsx','xls'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qKKxFKS7SqFx",
        "outputId": "ad37792e-e569-40be-d441-9ac3e0233256"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 175
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#046 startswith 메서드\n",
        "#파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.\n",
        "\n",
        "file_name = \"2020_보고서.xlsx\"\n",
        "file_name.startswith('2020')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P1WQgI2ESvrD",
        "outputId": "6620b516-d59c-436e-b2d2-f0ea65bcaad6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 176
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#047 split 메서드\n",
        "#다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.\n",
        "\n",
        "a = \"hello world\"\n",
        "b = a.split(' ')\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rcKirlAOS1fL",
        "outputId": "9887ed40-f547-4254-f541-a75ad8f439a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['hello', 'world']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#048 split 메서드\n",
        "#다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.\n",
        "\n",
        "ticker = \"btc_krw\"\n",
        "print(ticker.split('_'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sIRH_dfCS3i8",
        "outputId": "7cc01e8d-2c41-4224-e3b2-9a325ee3323e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['btc', 'krw']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#049 split 메서드\n",
        "#다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.\n",
        "\n",
        "date = \"2020-05-01\"\n",
        "dt = date.split('-')\n",
        "print(dt[0]+'년',dt[1]+'월',dt[2]+'일')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dgKhIXCrS6D4",
        "outputId": "76ba73db-011b-40a7-e192-a005a7fe3a8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2020년 05월 01일\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#050 rstrip 메서드\n",
        "#문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.\n",
        "\n",
        "data = \"039490     \"\n",
        "data.rstrip()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "OYztYp0gS8ZG",
        "outputId": "c3a2d422-ae5c-4e26-8a27-ba2b3e14f262"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'039490'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 166
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###DAY2\n",
        "dict references : https://wikidocs.net/16 , https://dojang.io/mod/page/view.php?id=2307"
      ],
      "metadata": {
        "id": "aA6b61SbDhuN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#051 리스트 생성\n",
        "#2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)\n",
        "#순위\t영화\n",
        "#1\t닥터 스트레인지\n",
        "#2\t스플릿\n",
        "#3\t럭키\n",
        "movie_rank = ['닥터 스트레인지','스플릿','럭키']\n",
        "type(movie_rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fxxqaark6LTZ",
        "outputId": "0377ce9d-3979-43f2-dc44-439bd9d4596e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#052 리스트에 원소 추가\n",
        "#051의 movie_rank 리스트에 \"배트맨\"을 추가하라.\n",
        "movie_rank.append(\"배트맨\")\n",
        "print(movie_rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zg_PCJho6LQS",
        "outputId": "8446cb86-fb01-4f31-fe17-d5b436965eea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['닥터 스트레인지', '스플릿', '럭키', '배트맨']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#053 (insert 사용 = insert(인덱스,원소))\n",
        "#movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. \"슈퍼맨\"을 \"닥터 스트레인지\"와 \"스플릿\" 사이에 추가하라.\n",
        "#movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']\n",
        "movie_rank.insert(1,'슈퍼맨')\n",
        "print(movie_rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bJKAf9VV6LJU",
        "outputId": "1a75144e-b09b-4edb-cbb0-7d1d4811d917"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#054\n",
        "#movie_rank 리스트에서 '럭키'를 삭제하라.\n",
        "movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']\n",
        "movie_rank[3]\n",
        "del movie_rank[3]\n",
        "print(movie_rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NlV_6Wlp6K_U",
        "outputId": "4160e885-0abc-43a3-9441-ba32bee41042"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#055\n",
        "#movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.\n",
        "movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']\n",
        "movie_rank[-2:]\n",
        "del movie_rank[-2:]\n",
        "print(movie_rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o3EFSn7u6K4H",
        "outputId": "b3d27a1e-808a-48ad-bda3-c30475e24797"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['닥터 스트레인지', '슈퍼맨']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#056\n",
        "#lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.\n",
        "lang1 = [\"C\", \"C++\", \"JAVA\"]\n",
        "lang2 = [\"Python\", \"Go\", \"C#\"]\n",
        "#실행 예: langs >> ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']\n",
        "langs = lang1 + lang2\n",
        "print(langs)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nY1gh6sy6Ku-",
        "outputId": "db648d5e-3d33-4e29-f3b5-f5edccb336f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#057\n",
        "#다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)\n",
        "\n",
        "nums = [1, 2, 3, 4, 5, 6, 7]\n",
        "#실행 예: max:  7 min:  1\n",
        "print(f'min: {min(nums)}\\nmax: {max(nums)}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QPkhbGgd6Kkh",
        "outputId": "61971232-6df6-41bd-f346-aaec84eb8d54"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "min: 1\n",
            "max: 7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#058\n",
        "#다음 리스트의 합을 출력하라.\n",
        "\n",
        "nums = [1, 2, 3, 4, 5]\n",
        "#실행 예:15\n",
        "print(sum(nums))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7JZrNGkM6Kg4",
        "outputId": "e25c3a7a-541c-4e7e-bd50-75132860703e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#059\n",
        "#다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.\n",
        "\n",
        "cook = [\"피자\", \"김밥\", \"만두\", \"양념치킨\", \"족발\", \"피자\", \"김치만두\", \"쫄면\", \"소시지\", \"라면\", \"팥빙수\", \"김치전\"]\n",
        "print(len(cook))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gOcUmT8m6KeA",
        "outputId": "3eed3051-b5e9-4329-f6c9-e40861a1148f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#060\n",
        "#다음 리스트의 평균을 출력하라.\n",
        "\n",
        "nums = [1, 2, 3, 4, 5]\n",
        "#실행 예: 3.0\n",
        "avrg = sum(nums)/len(nums)\n",
        "print(avrg)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kVTETpu56KaX",
        "outputId": "3d9f0a20-f45c-4c1b-a348-c2555afbe671"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#061\n",
        "#price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)\n",
        "\n",
        "price = ['20180728', 100, 130, 140, 150, 160, 170]\n",
        "#출력 예시:[100, 130, 140, 150, 160, 170]\n",
        "\n",
        "print(price[1:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FN5hkDBo6KQO",
        "outputId": "34f149b3-3732-4feb-fc2f-dd5c7b4d57d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[100, 130, 140, 150, 160, 170]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#062\n",
        "#슬라이싱을 사용해서 홀수만 출력하라.\n",
        "\n",
        "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "#실행 예:[1, 3, 5, 7, 9]\n",
        "\n",
        "print(nums[::2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mig0bcpnFGQT",
        "outputId": "eed28779-9ad8-4218-87cd-7fb3fce025f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 3, 5, 7, 9]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#063\n",
        "#슬라이싱을 사용해서 짝수만 출력하라.\n",
        "\n",
        "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "#실행 예:[2, 4, 6, 8, 10]\n",
        "\n",
        "print(nums[1::2]) #start from 1 hop 1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vgklrnaqFIYq",
        "outputId": "97d0d050-a406-40fd-e1ad-7fa036c3e573"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 4, 6, 8, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#064\n",
        "#슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.\n",
        "\n",
        "nums = [1, 2, 3, 4, 5]\n",
        "#실행 예:[5, 4, 3, 2, 1]\n",
        "\n",
        "print(nums[::-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xwMeLVG1FMSo",
        "outputId": "a20d29ed-6968-4ada-b4d6-261bf24a9b68"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 4, 3, 2, 1]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#065\n",
        "#interest 리스트에는 아래의 데이터가 바인딩되어 있다.\n",
        "\n",
        "interest = ['삼성전자', 'LG전자', 'Naver']\n",
        "#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.\n",
        "#출력 예시:삼성전자 Naver\n",
        "\n",
        "print(interest[0], interest[2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NHInk96OFP8N",
        "outputId": "c321202a-7b56-4505-c12e-38b21c39d4f9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "삼성전자 Naver\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#066 join 메서드\n",
        "#interest 리스트에는 아래의 데이터가 바인딩되어 있다.\n",
        "\n",
        "interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']\n",
        "#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.\n",
        "#출력 예시:삼성전자 LG전자 Naver SK하이닉스 미래에셋대우\n",
        "\n",
        "for i in interest:\n",
        "  print(f'{i}',end=' ')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RTxsrnG7FYYC",
        "outputId": "9638fd94-e160-4a1c-c83c-8fc54e73a56b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "삼성전자 LG전자 Naver SK하이닉스 미래에셋대우 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#067 join 메서드\n",
        "#interest 리스트에는 아래의 데이터가 바인딩되어 있다.\n",
        "\n",
        "interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']\n",
        "#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.\n",
        "#출력 예시:삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우\n",
        "print(\"/\".join(interest))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nQCyxaHMFbot",
        "outputId": "226ad547-4263-49bb-b5dd-b1ee80d0fc3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#068 join 메서드\n",
        "#interest 리스트에는 아래의 데이터가 바인딩되어 있다.\n",
        "\n",
        "interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']\n",
        "#join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.\n",
        "#출력 예시:\n",
        "#삼성전자\n",
        "#LG전자\n",
        "#Naver\n",
        "#SK하이닉스\n",
        "#미래에셋대우\n",
        "print(\"\\n\".join(interest))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4pj4kMU8FfTA",
        "outputId": "7b919083-8a8f-448d-c49c-22a88ae7ba83"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "삼성전자\n",
            "LG전자\n",
            "Naver\n",
            "SK하이닉스\n",
            "미래에셋대우\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#069 문자열 split 메서드\n",
        "#회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.\n",
        "\n",
        "string = \"삼성전자/LG전자/Naver\"\n",
        "#이를 interest 이름의 리스트로 분리 저장하라.\n",
        "\n",
        "#실행 예시\n",
        "#>> print(interest)\n",
        "#['삼성전자', 'LG전자', 'Naver']\n",
        "\n",
        "print(string.split('/'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xc_pzs_jFivq",
        "outputId": "3b967c28-486d-4f67-cb05-402d5b1a2965"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['삼성전자', 'LG전자', 'Naver']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#070 리스트 정렬\n",
        "#리스트에 있는 값을 오름차순으로 정렬하세요.\n",
        "\n",
        "data = [2, 4, 3, 1, 5, 10, 9]\n",
        "data.sort()\n",
        "print(data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FlLY3GsKFzdb",
        "outputId": "cf37c09b-68f6-457a-cbd2-2b18f31bacb6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5, 9, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#071\n",
        "#my_variable 이름의 비어있는 튜플을 만들라.\n",
        "\n",
        "my_variable = ()\n",
        "type(my_variable)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "znFwyKICPKY0",
        "outputId": "8b002d9c-e494-4680-8ee0-01b85650e1a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tuple"
            ]
          },
          "metadata": {},
          "execution_count": 159
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#072\n",
        "#2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)\n",
        "\n",
        "#순위\t영화\n",
        "#1\t닥터 스트레인지\n",
        "#2\t스플릿\n",
        "#3\t럭키\n",
        "\n",
        "movie_rank = ('닥터 스트레인지','스플릿','럭키')\n",
        "print(movie_rank,type(movie_rank))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ll3e_aGWPurQ",
        "outputId": "53523403-7a83-40d0-dc1c-1f01f46689d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('닥터 스트레인지', '스플릿', '럭키') <class 'tuple'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#073\n",
        "#숫자 1 이 저장된 튜플을 생성하라.\n",
        "  \n",
        "t = (1)\n",
        "tuple1 = (1,)\n",
        "print(t,type(t),tuple1,type(tuple1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qzA0n0quPzyI",
        "outputId": "942a4ea7-5a6f-467c-d4ac-1f51b504ec95"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 <class 'int'> (1,) <class 'tuple'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#074\n",
        "#다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.\n",
        "\n",
        "#>> t = (1, 2, 3)\n",
        "#>> t[0] = 'a'\n",
        "#Traceback (most recent call last):\n",
        "#  File \"<pyshell#46>\", line 1, in <module>\n",
        "#    t[0] = 'a'\n",
        "#TypeError: 'tuple' object does not support item assignment\n",
        "\n",
        "print('원소값 변경이 불가능합니다.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "94NCiUYgQLza",
        "outputId": "546c068e-552c-4c2d-8954-22b11ae2c04f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "원소값 변경이 불가능합니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#075\n",
        "#아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?\n",
        "\n",
        "t = 1, 2, 3, 4\n",
        "\n",
        "\n",
        "a = type(t)\n",
        "print(f\"t의 데이터 타입은 {a}입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zq8LoD4tQQSU",
        "outputId": "dd449acb-f0cd-48f9-b042-eaee25572509"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "t의 데이터 타입은 <class 'tuple'>입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#076\n",
        "#변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.\n",
        "\n",
        "t = ('a', 'b', 'c')\n",
        "del t\n",
        "\n",
        "t = ('A', 'b', 'c')\n",
        "print(t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-3s_Z4_sQS8A",
        "outputId": "c45b8198-850d-4dba-c177-2088e96dfc8d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('A', 'b', 'c')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#077\n",
        "#다음 튜플을 리스트로 변환하라.\n",
        "interest = ('삼성전자', 'LG전자', 'SK Hynix')\n",
        "\n",
        "into = list(interest)\n",
        "print(type(into))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H3KFfEgdQVKG",
        "outputId": "aa002be1-4389-461c-cb07-c3c4e47da0e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#078\n",
        "#다음 리스트를 튜플로 변경하라.\n",
        "\n",
        "interest = ['삼성전자', 'LG전자', 'SK Hynix']\n",
        "\n",
        "into = tuple(interest)\n",
        "print(type(into))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pwJuoKP9QXNj",
        "outputId": "0d66571d-80dd-43dd-8a39-cf2dcc0c3e15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'tuple'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#079 튜플 언팩킹\n",
        "#다음 코드의 실행 결과를 예상하라.\n",
        "\n",
        "temp = ('apple', 'banana', 'cake')\n",
        "a, b, c = temp\n",
        "print(a, b, c)\n",
        "\n",
        "#temp 안에 있는 원소가 a, b, c 에 지정됨 "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_oG79RdrQaTA",
        "outputId": "d2b24c8c-181b-4aba-8451-ebefcef3db7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "apple banana cake\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#080 range 함수\n",
        "#1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.\n",
        "#(2, 4, 6, 8 ... 98)\n",
        "a = tuple(range(2,99,2)) #start-end-gap\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qzyMZeGAQcAq",
        "outputId": "7ff0a313-99ce-40f2-f54b-54f147a82441"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#081 별 표현식\n",
        "#기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. \n",
        "#하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.\n",
        "\n",
        "#>> a, b, *c = (0, 1, 2, 3, 4, 5)\n",
        "#>> a\n",
        "#0\n",
        "#>> b\n",
        "#1\n",
        "#>> c\n",
        "#[2, 3, 4, 5]\n",
        "#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.\n",
        "\n",
        "#scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]\n",
        "\n",
        "scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]\n",
        "*valid_score, _, _= scores\n",
        "print(valid_score)"
      ],
      "metadata": {
        "id": "0qaM0Wm0YZpj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5adeecfd-d7b5-4f01-d575-33fba48289b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#082\n",
        "#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.\n",
        "\n",
        "scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]\n",
        "\n",
        "a,b,*vaild_score = scores\n",
        "print(vaild_score)"
      ],
      "metadata": {
        "id": "eHpD1Pnwau6Y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ae50bbf0-bed9-413b-f563-792e60ab4c93"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#083\n",
        "#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.\n",
        "\n",
        "scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]\n",
        "\n",
        "len(scores)\n",
        "a,*vaild_score,b = scores\n",
        "print(vaild_score)"
      ],
      "metadata": {
        "id": "ccKFI1yUayTI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4d0761fc-4d35-42fd-dd25-c1525575e534"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#084 비어있는 딕셔너리\n",
        "#temp 이름의 비어있는 딕셔너리를 만들라.\n",
        "\n",
        "temp = {}\n",
        "print(type(temp))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QrTzzAzAa1I4",
        "outputId": "454ae31e-cf35-4722-eab6-4ebcb84e98e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'dict'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#085\n",
        "#다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.\n",
        "\n",
        "#이름\t희망 가격\n",
        "#메로나\t1000\n",
        "#폴라포\t1200\n",
        "#빵빠레\t1800\n",
        "icecream = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800 }"
      ],
      "metadata": {
        "id": "urwjScwLa28c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#086\n",
        "#085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.\n",
        "\n",
        "#이름\t희망 가격\n",
        "#죠스바\t1200\n",
        "#월드콘\t1500\n",
        "icecream['죠스바'] = '1200'\n",
        "icecream['월드콘'] = '1500'\n",
        "print(icecream)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cAdeHeJpeCa5",
        "outputId": "da8502c5-9d1d-40a9-809e-19a2f6f9b325"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': '1200', '월드콘': '1500'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#087\n",
        "#다음 딕셔너리를 사용하여 메로나 가격을 출력하라.\n",
        "\n",
        "ice = {'메로나': 1000,\n",
        "       '폴로포': 1200,\n",
        "       '빵빠레': 1800,\n",
        "       '죠스바': 1200,\n",
        "       '월드콘': 1500}\n",
        "#실행 예:메로나 가격: 1000\n",
        "a = ice['메로나']\n",
        "print(f'메로나 가격: {a}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qXqpuUYNd02T",
        "outputId": "b55fdadb-a838-4c7d-ffd7-9355fb726fbb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "메로나 가격: 1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#088\n",
        "#다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.\n",
        "\n",
        "ice = {'메로나': 1000,\n",
        "       '폴로포': 1200,\n",
        "       '빵빠레': 1800,\n",
        "       '죠스바': 1200,\n",
        "       '월드콘': 1500}\n",
        "ice.update(메로나 = 1300)\n",
        "print(ice)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VQNZTXH6dVjr",
        "outputId": "95159590-4cf6-4520-bbae-243856dccf21"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'메로나': 1300, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#089\n",
        "#다음 딕셔너리에서 메로나를 삭제하라.\n",
        "\n",
        "ice = {'메로나': 1000,\n",
        "       '폴로포': 1200,\n",
        "       '빵빠레': 1800,\n",
        "       '죠스바': 1200,\n",
        "       '월드콘': 1500}\n",
        "del ice['메로나']\n",
        "print(ice)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "It5k5E2qdTAp",
        "outputId": "efd8d453-99ec-46ba-a44d-f07d16dc8670"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#090\n",
        "#다음 코드에서 에러가 발생한 원인을 설명하라.\n",
        "\n",
        "#>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\n",
        "#>> icecream['누가바']\n",
        "#Traceback (most recent call last):\n",
        "# File \"<pyshell#69>\", line 1, in <module>\n",
        "#   icecream['누가바']\n",
        "#KeyError: '누가바'\n",
        "\n",
        "print('누가바 is not exist in dictionary {icecream}')"
      ],
      "metadata": {
        "id": "kTp9Ra36dI4_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a5ba119d-44f7-407c-92df-6f5c9e315ed5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "누가바 is not exist in dictionary {icecream}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#091 딕셔너리 생성\n",
        "#아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.\n",
        "\n",
        "#이름\t가격\t재고\n",
        "#메로나\t300\t20\n",
        "#비비빅\t400\t3\n",
        "#죠스바\t250\t100\n",
        "inventory = {'메로나':[300,20],'죠스바':[250,100],'비비빅':[400,100]}\n",
        "print(inventory)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6KirNkyrdIRq",
        "outputId": "452782ef-fcc6-4675-9a18-01244c2c07c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'메로나': [300, 20], '죠스바': [250, 100], '비비빅': [400, 100]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#092 딕셔너리 인덱싱\n",
        "#inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.\n",
        "\n",
        "inventory = {\"메로나\": [300, 20],\n",
        "              \"비비빅\": [400, 3],\n",
        "              \"죠스바\": [250, 100]}\n",
        "#실행 예시:300 원\n",
        "\n",
        "price = inventory['메로나']\n",
        "#print(f'{price[0]}원')\n",
        "print('{}원'.format(price[0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tkNNBFcMdEjs",
        "outputId": "e2b0cff7-8275-4422-9d85-f834e05427cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "300원\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#093 딕셔너리 인덱싱\n",
        "#inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.\n",
        "\n",
        "inventory = {\"메로나\": [300, 20],\n",
        "              \"비비빅\": [400, 3],\n",
        "              \"죠스바\": [250, 100]}\n",
        "#실행 예시:20 개\n",
        "\n",
        "print(inventory['메로나'][1],'개')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FYOF4BUIcNLX",
        "outputId": "0c03a4cf-04cf-4ba2-d6ef-1375a7bb04ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20 개\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#094 딕셔너리 추가\n",
        "#inventory 딕셔너리에 아래 데이터를 추가하라.\n",
        "\n",
        "inventory = {\"메로나\": [300, 20],\n",
        "              \"비비빅\": [400, 3],\n",
        "              \"죠스바\": [250, 100]}\n",
        "#이름\t가격\t재고\n",
        "#월드콘\t500\t7\n",
        "\n",
        "#실행 예시:\n",
        "#>> print(inventory)\n",
        "#{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}\n",
        "\n",
        "\n",
        "inventory['월드콘']=[500,7]\n",
        "print(inventory)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gHJcY7pGcJVz",
        "outputId": "8828ce0b-3f11-4e9a-f77a-33b0e7a13d05"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#095 딕셔너리 keys() 메서드\n",
        "#다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.\n",
        "\n",
        "icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\n",
        "\n",
        "key_list=list(icecream.keys())\n",
        "print(key_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LM1j4N9bcC1T",
        "outputId": "4834a71c-82bd-4ffb-bd02-ed594f9d3e2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#096 딕셔너리 values() 메서드\n",
        "#다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.\n",
        "\n",
        "icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\n",
        "\n",
        "value_list=list(icecream.values())\n",
        "print(value_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EW9GxQyMcAr0",
        "outputId": "12622601-4ac0-4263-bb04-eebeead38706"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1200, 1200, 1800, 1500, 1000]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#097 딕셔너리 values() 메서드\n",
        "#icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.\n",
        "\n",
        "icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\n",
        "#출력 예시:6700\n",
        "print(sum(icecream.values()))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fVEx8ivvb9ng",
        "outputId": "f32a3ae2-a21d-4c8f-ae86-16f9de192b41"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6700\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#098 딕셔너리 update 메서드\n",
        "#아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.\n",
        "\n",
        "icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\n",
        "new_product = {'팥빙수':2700, '아맛나':1000}\n",
        "\n",
        "icecream.update(new_product)\n",
        "print(icecream)\n",
        "#실행 예시:\n",
        "#>> print(icecream)\n",
        "#{'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qYJg2zEGbShU",
        "outputId": "38528ef5-f193-4047-c135-b6dd38674140"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥빙수': 2700, '아맛나': 1000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#099 zip과 dict\n",
        "#아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.\n",
        "\n",
        "keys = (\"apple\", \"pear\", \"peach\")\n",
        "vals = (300, 250, 400)\n",
        "#실행 예시:\n",
        "#>> print(result)\n",
        "#{'apple': 300, 'pear': 250, 'peach': 400}\n",
        "\n",
        "\n",
        "result = dict(zip(keys, vals))\n",
        "print(result)"
      ],
      "metadata": {
        "id": "qbuG_DnVbPS2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6baa901d-4bea-4719-d094-e3b6c83e3515"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'apple': 300, 'pear': 250, 'peach': 400}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#100 zip과 dict\n",
        "#date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.\n",
        "\n",
        "date = ['09/05', '09/06', '09/07', '09/08', '09/09']\n",
        "close_price = [10500, 10300, 10100, 10800, 11000]\n",
        "#실행 예시:\n",
        "#>> print(close_table)\n",
        "#{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}\n",
        "\n",
        "close_table = dict(zip(date, close_price))\n",
        "print(close_table)"
      ],
      "metadata": {
        "id": "Ycw0nGR3bJ16",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b78fd5a0-3fe2-4e53-8097-f3b3539e1b27"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###D3"
      ],
      "metadata": {
        "id": "bPTd0fYygHSL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#101\n",
        "#파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?\n",
        "\n",
        "print(type(True),type(False),'입니다.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mvt_-ugWTfJ2",
        "outputId": "a9e3419b-2559-4e7c-9017-bdb58c11096c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'bool'> <class 'bool'> 입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#102\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "#print(3 == 5)\n",
        "\n",
        "print(\"3==5 is not true, 3!=5 so False will be printed,\",3 == 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r63yLSKZWNbM",
        "outputId": "d700ab86-265e-4fed-a963-45acff34244e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3==5 is not true, 3!=5 so False will be printed, False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#103\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "#print(3 < 5)\n",
        "\n",
        "if 3 < 5 :\n",
        "  print(True)\n",
        "else:\n",
        "  print(False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4LjiG1stWqFA",
        "outputId": "d768e55c-4f88-47c9-f35a-34b88f9fe15b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#104\n",
        "#아래 코드의 결과를 예상하라.\n",
        "\n",
        "#x = 4\n",
        "#print(1 < x < 5)\n",
        "\n",
        "print(True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m4YaU8RyWr0u",
        "outputId": "f7d03b54-4976-4de0-c60a-8e970abc5c0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#105\n",
        "#아래 코드의 결과를 예상하라.\n",
        "\n",
        "print ((3 == 3) and (4 != 3))\n",
        "\n",
        "print('3은 3이고 4는 3이 아니다 = True')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q8CnzbL6WnH_",
        "outputId": "6ac7789b-4d06-4e8c-85d9-7cd28d950ec8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "3은 3이고 4는 3이 아니다 = True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#106\n",
        "#아래 코드에서 에러가 발생하는 원인에 대해 설명하라.\n",
        "\n",
        "#print(3 => 4)\n",
        "print(3 >= 4)\n",
        "#부호를 잘못썼음"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-PA_Y8RfWlnV",
        "outputId": "7607177b-4b92-47cf-b3b8-50201acebad6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#107\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "\n",
        "if 4 < 3:\n",
        "    print(\"Hello World\")\n",
        "\n",
        "#프린트 되지 않는다. == False"
      ],
      "metadata": {
        "id": "07x2vokKWecA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#108\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "\n",
        "if 4 < 3:\n",
        "    print(\"Hello World.\")\n",
        "else:\n",
        "    print(\"Hi, there.\")\n",
        "\n",
        "#Hi, there."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hVllbLSXWbra",
        "outputId": "47620e33-495a-4071-a4b7-d0bf7e372d48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi, there.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#109\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "\n",
        "if True :\n",
        "    print (\"1\")\n",
        "    print (\"2\")\n",
        "else :\n",
        "    print(\"3\")\n",
        "print(\"4\")\n",
        "\n",
        "#1\n",
        "#2\n",
        "#4\n",
        "#왜..?"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ULn5hhShWWch",
        "outputId": "55034ca8-85b2-4077-cb9a-4fbc7697fde2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#110\n",
        "#아래 코드의 출력 결과를 예상하라\n",
        "\n",
        "if True :\n",
        "    if False:\n",
        "        print(\"1\")\n",
        "        print(\"2\")\n",
        "    else:\n",
        "        print(\"3\")\n",
        "else :\n",
        "    print(\"4\")\n",
        "print(\"5\")\n",
        " \n",
        "#3\n",
        "#5\n",
        "#idk"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CU0S5jl8WVyV",
        "outputId": "eb6fee87-04ca-438b-b2a8-c946e0e42fb0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#111\n",
        "#사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 \"안녕하세요\"를 입력한 경우의 출력 결과이다.\n",
        "\n",
        "#>> 안녕하세요\n",
        "#안녕하세요안녕하세요\n",
        "\n",
        "print(input()*2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GYgrYho1ToJR",
        "outputId": "1aee61c5-ca39-4bb8-8171-ead9f77b2b38"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "안녕하세요\n",
            "안녕하세요안녕하세요\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#112\n",
        "#사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.\n",
        "\n",
        "#>> 숫자를 입력하세요: 30\n",
        "#40\n",
        "num = input('숫자를 입력하세요: ')\n",
        "print(int(num)+10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sgTB6AJUUnKy",
        "outputId": "398077f2-d481-4fbc-9a16-ea0a23b12d81"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "숫자를 입력하세요: 30\n",
            "40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#113\n",
        "#사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.\n",
        "\n",
        "#>> 30\n",
        "#짝수\n",
        "\n",
        "a = input()\n",
        "if int(a)%2 == 1 :\n",
        "  print(\"홀수\")\n",
        "else:\n",
        "  print(\"짝수\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W4BXtUxIUr4Y",
        "outputId": "fb7889fa-a35b-4242-96fc-a224fb4aa8bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "짝수\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#114\n",
        "#사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.\n",
        "\n",
        "#>> 입력값: 200\n",
        "#출력값: 220\n",
        "#>> 입력값: 240\n",
        "#출력값: 255\n",
        "\n",
        "i = input()\n",
        "num = int(i)+20 \n",
        "if num > 255:\n",
        "    print(255)\n",
        "else:\n",
        "    print(num)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rFEmBKmrUwig",
        "outputId": "12ae9d59-11e3-4ae1-8b11-07787d62bb09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "999\n",
            "255\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#115\n",
        "#사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. \n",
        "#단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.\n",
        "\n",
        "#>> 입력값: 200\n",
        "#출력값: 180\n",
        "#>> 입력값: 15\n",
        "#출력값: 0\n",
        "\n",
        "a = input('입력값:')\n",
        "\n",
        "if int(a) < 0:\n",
        "  print(0)\n",
        "elif int(a) > 255:\n",
        "  print(255)\n",
        "else:\n",
        "   print(a)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZMVm6_HdUz0Z",
        "outputId": "9415b15c-a2ae-4b86-8a75-0d25a7ab02b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "입력값:-11\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#116\n",
        "#사용자로부터 입력 받은 시간이 정각인지 판별하라.\n",
        "\n",
        "#>> 현재시간:02:00\n",
        "#정각 입니다.\n",
        "#>> 현재시간:03:10\n",
        "#정각이 아닙니다\n",
        "\n",
        "time = input(\"현재시간: \")\n",
        "if time[-2:] == \"00\":\n",
        "    print(\"정각 입니다.\")\n",
        "else:\n",
        "    print(\"정각이 아닙니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cMcqqVT7U3m2",
        "outputId": "4d5ebd9e-fb58-469b-c186-10e797e9ed5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "현재시간: 2:15\n",
            "정각이 아닙니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#117\n",
        "#사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 \"정답입니다\"를 아닐 경우 \"오답입니다\" 출력하라.\n",
        "\n",
        "fruit = [\"사과\", \"포도\", \"홍시\"]\n",
        "#>> 좋아하는 과일은? 사과\n",
        "#정답입니다.\n",
        "\n",
        "a = input('좋아하는 과일은? ')\n",
        "if a in fruit:\n",
        "  print(\"정답입니다\")\n",
        "else:\n",
        "  print(\"오답입니다\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2aLK7dfaU89C",
        "outputId": "bab74ff4-00de-44db-8c34-d0ba57b00eae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "좋아하는 과일은? 사과\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#118\n",
        "#투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 \"투자 경고 종목이 아닙니다.\"를 출력하는 프로그램을 작성하라.\n",
        "\n",
        "warn_investment_list = [\"Microsoft\", \"Google\", \"Naver\", \"Kakao\", \"SAMSUNG\", \"LG\"]\n",
        "\n",
        "a = input('투자 목록 입력: ')\n",
        "if a in warn_investment_list:\n",
        "  print('투자 경고 종목입니다')\n",
        "else:\n",
        "  print('투자 경고 종목이 아닙니다.')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DiQTwGlQU_8s",
        "outputId": "24e3a1ed-316f-4893-c9b2-3feb79e0a0eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "투자 목록 입력: 삼성\n",
            "투자 경고 종목이 아닙니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#119\n",
        "#아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 \"정답입니다\"를 아닐 경우 \"오답입니다\" 출력하라.\n",
        "\n",
        "fruit = {\"봄\" : \"딸기\", \"여름\" : \"토마토\", \"가을\" : \"사과\"}\n",
        "#>> 제가좋아하는계절은: 봄\n",
        "#정답입니다.\n",
        "\n",
        "a = input('제가 좋아하는 계절은 : ')\n",
        "\n",
        "if a in fruit:\n",
        "    print(\"정답입니다.\")\n",
        "else:\n",
        "    print(\"오답입니다.\")"
      ],
      "metadata": {
        "id": "LokxX6j-VCeN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#120\n",
        "#아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 \"정답입니다\"를 아닐 경우 \"오답입니다\" 출력하라.\n",
        "\n",
        "fruit = {\"봄\" : \"딸기\", \"여름\" : \"토마토\", \"가을\" : \"사과\"}\n",
        "#>> 좋아하는과일은? 한라봉\n",
        "#오답입니다.\n",
        "\n",
        "a = input('좋아하는과일은? ')\n",
        "\n",
        "if a in fruit.values():\n",
        "    print(\"정답입니다.\")\n",
        "else:\n",
        "    print(\"오답입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iXTSANtGVECJ",
        "outputId": "cacc03a8-eb00-4eaa-b9d9-58ecabf2fcf7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "좋아하는과일은? 한라봉\n",
            "오답입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#121\n",
        "#사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.\n",
        "\n",
        "#>> a\n",
        "#A\n",
        "#힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. \n",
        "#힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.\n",
        "\n",
        "abc = input(\"\")\n",
        "if abc.islower():\n",
        "    print(abc.upper())\n",
        "else:\n",
        "    print(abc.lower())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UYUZRW8kUS1P",
        "outputId": "2c3e1259-36c7-4d55-da58-7bd0861340e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "G\n",
            "g\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#122\n",
        "#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.\n",
        "\n",
        "#점수\t학점\n",
        "#81~100\tA\n",
        "#61~80\tB\n",
        "#41~60\tC\n",
        "#21~40\tD\n",
        "#0~20\tE\n",
        "#>> score: 83\n",
        "#grade is A\n",
        "\n",
        "score = input(\"score: \")\n",
        "score = int(score)\n",
        "if 81 <= score <= 100:\n",
        "    print(\"grade is A\")\n",
        "elif 61 <= score <= 80:\n",
        "    print(\"grade is B\")\n",
        "elif 41 <= score <= 60:\n",
        "    print(\"grade is C\")\n",
        "elif 21 <= score <= 40:\n",
        "    print(\"grade is D\")\n",
        "else:\n",
        "    print(\"grade is E\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "veBP-tAcVIQA",
        "outputId": "14514043-c90b-49f4-ca90-6cae79ced047"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "score: 55\n",
            "grade is C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#123\n",
        "#사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. \n",
        "#각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.\n",
        "\n",
        "#통화명\t환율\n",
        "#달러\t1167\n",
        "#엔\t1.096\n",
        "#유로\t1268\n",
        "#위안\t171\n",
        "#>> 입력: 100 달러\n",
        "#116700.00 원\n",
        "\n"
      ],
      "metadata": {
        "id": "vp5-9nzYVTcl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#124\n",
        "#사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.\n",
        "\n",
        "#>> input number1: 10\n",
        "#>> input number2: 9\n",
        "#>> input number3: 20\n",
        "#20\n"
      ],
      "metadata": {
        "id": "kRjpylxbVdD8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#125\n",
        "#휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.\n",
        "\n",
        "#번호\t통신사\n",
        "#011\tSKT\n",
        "#016\tKT\n",
        "#019\tLGU\n",
        "#010\t알수없음\n",
        "#>> 휴대전화 번호 입력: 011-345-1922\n",
        "#당신은 SKT 사용자입니다.\n",
        "\n",
        "tele = {SKT:011,KT:016,LGU:019,알수없음:010}\n",
        "\n",
        "f\"당신은 {tele} 사용자입니다.\"\n",
        "\n"
      ],
      "metadata": {
        "id": "1js8dNz-Vlqw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#126\n",
        "#우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.\n",
        "\n",
        "#-\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n",
        "#01\t강북구\t강북구\t강북구\t도봉구\t도봉구\t도봉구\t노원구\t노원구\t노원구\t노원구\n",
        "#사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라\n",
        "\n",
        "#>> 우편번호: 01400\n",
        "#도봉구\n"
      ],
      "metadata": {
        "id": "3-cvzRORVre1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#127\n",
        "#주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.\n",
        "\n",
        "#>> 주민등록번호: 821010-1635210\n",
        "#남자\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "N7Ac_o2jVzIJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#128\n",
        "#주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라\n",
        "\n",
        "#지역코드\t출생지\n",
        "#00 ~ 08\t서울\n",
        "#09 ~ 12\t부산\n",
        "#>> 주민등록번호: 821010-1635210\n",
        "#서울이 아닙니다.\n",
        "#>> 주민등록번호: 861010-1015210\n",
        "#서울 입니다."
      ],
      "metadata": {
        "id": "u7r-e6BdV8nK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#129\n",
        "#주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.\n",
        "\n",
        " # 8 2 1 0 1 0 - 1 6 3 5 2 1 0\n",
        "#x 2 3 4 5 6 7   8 9 2 3 4 5 \n",
        "#-----------------------------\n",
        "#1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7\n",
        "#2차 계산: 11 -7 = 4\n",
        "#위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.\n",
        "\n",
        "#다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.\n",
        "\n",
        "#>> 주민등록번호: 821010-1635210\n",
        "#유효하지 않은 주민등록번호입니다. \n"
      ],
      "metadata": {
        "id": "IBUTm3c1V8fX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#130\n",
        "#아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.\n",
        "\n",
        "#import requests\n",
        "#btc = requests.get(\"https://api.bithumb.com/public/ticker/\").json()['data']\n",
        "#btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 \"상승장\", 그렇지 않은 경우 \"하락장\" 문자열을 출력하라.\n",
        "\n",
        "#Key Name\tDescription\n",
        "#opening_price\t최근 24시간 내 시작 거래금액\n",
        "#closing_price\t최근 24시간 내 마지막 거래금액\n",
        "#min_price\t최근 24시간 내 최저 거래금액\n",
        "#max_price\t최근 24시간 내 최고 거래금액"
      ],
      "metadata": {
        "id": "x0ROIyFeWB1i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#131\n",
        "#for문의 실행결과를 예측하라.\n",
        "\n",
        "#과일 = [\"사과\", \"귤\", \"수박\"]\n",
        "#for 변수 in 과일:\n",
        "#    print(변수)\n",
        "\n"
      ],
      "metadata": {
        "id": "swUpdpMSUbtz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#132\n",
        "#for문의 실행결과를 예측하라.\n",
        "\n",
        "#과일 = [\"사과\", \"귤\", \"수박\"]\n",
        "#for 변수 in 과일:\n",
        "#  print(\"#####\")\n"
      ],
      "metadata": {
        "id": "Nha5KOmlX57X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#133\n",
        "#다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.\n",
        "\n",
        "#for 변수 in [\"A\", \"B\", \"C\"]:\n",
        "#  print(변수)"
      ],
      "metadata": {
        "id": "WawvEj7zX8RD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#134\n",
        "#for문을 풀어서 동일한 동작을하는 코드를 작성하라.\n",
        "\n",
        "#for 변수 in [\"A\", \"B\", \"C\"]:\n",
        "#  print(\"출력:\", 변수)\n"
      ],
      "metadata": {
        "id": "0HSGW5RvXhFB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#135\n",
        "#for문을 풀어서 동일한 동작을 하는 코드를 작성하라.\n",
        "\n",
        "#for 변수 in [\"A\", \"B\", \"C\"]:\n",
        "#  b = 변수.lower()\n",
        "#  print(\"변환:\", b)"
      ],
      "metadata": {
        "id": "8NjF2d3OXjN9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#136\n",
        "#다음 코드를 for문으로 작성하라.\n",
        "\n",
        "#변수 = 10\n",
        "#print(변수)\n",
        "#변수 = 20\n",
        "#print(변수)\n",
        "#변수 = 30\n",
        "#print(변수)\n"
      ],
      "metadata": {
        "id": "pSojSHeKXek1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#137\n",
        "#다음 코드를 for문으로 작성하라.\n",
        "\n",
        "#print(10)\n",
        "#print(20)\n",
        "#print(30)"
      ],
      "metadata": {
        "id": "Bm3-maI1XcSA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#138\n",
        "#다음 코드를 for문으로 작성하라.\n",
        "\n",
        "#print(10)\n",
        "#print(\"-------\")\n",
        "#print(20)\n",
        "#print(\"-------\")\n",
        "#print(30)\n",
        "#print(\"-------\")\n"
      ],
      "metadata": {
        "id": "yvuWzgQ_XZGF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#139\n",
        "#다음 코드를 for문으로 작성하라.\n",
        "\n",
        "#print(\"++++\")\n",
        "#print(10)\n",
        "#print(20)\n",
        "#print(30)"
      ],
      "metadata": {
        "id": "vNzE-k99XUOY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#140\n",
        "#다음 코드를 for문으로 작성하라.\n",
        "\n",
        "#print(\"-------\")\n",
        "#print(\"-------\")\n",
        "#print(\"-------\")\n",
        "#print(\"-------\")"
      ],
      "metadata": {
        "id": "sgYay0m2XULe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#141\n",
        "#다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.\n",
        "\n",
        "#리스트 = [100, 200, 300]\n",
        "#110\n",
        "#210\n",
        "#310\n",
        "\n"
      ],
      "metadata": {
        "id": "sjaGkUtMUgqs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#142\n",
        "#for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.\n",
        "\n",
        "#리스트 = [\"김밥\", \"라면\", \"튀김\"]\n",
        "#오늘의 메뉴: 김밥\n",
        "#오늘의 메뉴: 라면\n",
        "#오늘의 메뉴: 튀김\n",
        "\n"
      ],
      "metadata": {
        "id": "vUGXFewCXQfl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#143\n",
        "#리스트에 주식 종목이름이 저장돼 있다.\n",
        "\n",
        "#리스트 = [\"SK하이닉스\", \"삼성전자\", \"LG전자\"]\n",
        "#저장된 문자열의 길이를 다음과 같이 출력하라.\n",
        "\n",
        "#6\n",
        "#4\n",
        "#4"
      ],
      "metadata": {
        "id": "Pka9uhV6XC-g"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#144\n",
        "#리스트에는 동물이름이 문자열로 저장돼 있다.\n",
        "\n",
        "#리스트 = ['dog', 'cat', 'parrot']\n",
        "#동물 이름과 글자수를 다음과 같이 출력하라.\n",
        "\n",
        "#dog 3\n",
        "#cat 3\n",
        "#parrot 6\n"
      ],
      "metadata": {
        "id": "K811J0KpXAWP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#145\n",
        "#리스트에 동물 이름 저장돼 있다.\n",
        "\n",
        "#리스트 = ['dog', 'cat', 'parrot']\n",
        "#for문을 사용해서 동물 이름의 첫 글자만 출력하라.\n",
        "\n",
        "#d\n",
        "#c\n",
        "#p\n"
      ],
      "metadata": {
        "id": "ht4Hw_vKW-B2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#146\n",
        "#리스트에는 세 개의 숫자가 바인딩돼 있다.\n",
        "\n",
        "#리스트 = [1, 2, 3]\n",
        "#for문을 사용해서 다음과 같이 출력하라.\n",
        "\n",
        "#3 x 1\n",
        "#3 x 2\n",
        "#3 x 3\n"
      ],
      "metadata": {
        "id": "Zn9Kv1_2W79B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#147\n",
        "#리스트에는 세 개의 숫자가 바인딩돼 있다.\n",
        "\n",
        "#리스트 = [1, 2, 3]\n",
        "#for문을 사용해서 다음과 같이 출력하라.\n",
        "\n",
        "#3 x 1 = 3\n",
        "#3 x 2 = 6\n",
        "#3 x 3 = 9"
      ],
      "metadata": {
        "id": "eJt8eSHyW5bz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#148\n",
        "#리스트에는 네 개의 문자열이 바인딩돼 있다.\n",
        "\n",
        "#리스트 = [\"가\", \"나\", \"다\", \"라\"]\n",
        "#for문을 사용해서 다음과 같이 출력하라.\n",
        "\n",
        "#나\n",
        "#다\n",
        "#라"
      ],
      "metadata": {
        "id": "Mw5S8s4wW3cw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#149\n",
        "#리스트에는 네 개의 문자열이 바인딩돼 있다.\n",
        "\n",
        "#리스트 = [\"가\", \"나\", \"다\", \"라\"]\n",
        "#for문을 사용해서 다음과 같이 출력하라.\n",
        "\n",
        "#가\n",
        "#다"
      ],
      "metadata": {
        "id": "PVTRtvwoW0uw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#150\n",
        "#리스트에는 네 개의 문자열이 바인딩돼 있다.\n",
        "\n",
        "#리스트 = [\"가\", \"나\", \"다\", \"라\"]\n",
        "#for문을 사용해서 다음과 같이 출력하라.\n",
        "\n",
        "#라\n",
        "#다\n",
        "#나\n",
        "#가"
      ],
      "metadata": {
        "id": "GZh1pxX8WxP2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}