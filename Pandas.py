{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Урок 2. Python. Работа с библиотекой Pandas. Часть 1.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vDGysueC1TNZ"
      },
      "source": [
        "# Загрузка данных"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Xg-tMZLxV7NV"
      },
      "source": [
        "# Импортируем в свой скрипт библиотеку Pandas\n",
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AaVwx9iqV9ft"
      },
      "source": [
        "# Загружаем данные в Python c помощью бибилиотеки Pandas\n",
        "df = pd.read_csv('advertising.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uEAYZQXUidad"
      },
      "source": [
        "# У метода read есть доп. параметры, которые можно указывать в скобках: \n",
        "df = pd.read_csv('advertising.csv', header = 0, sep = ',')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QospXaLpheYV",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "cd2bb62b-0655-4a80-bb51-59b192076328"
      },
      "source": [
        "# Возвратим первые 5 строк загруженного датафрейма\n",
        "df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>68.95</td>\n",
              "      <td>35</td>\n",
              "      <td>61833.90</td>\n",
              "      <td>256.09</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>0</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>80.23</td>\n",
              "      <td>31</td>\n",
              "      <td>68441.85</td>\n",
              "      <td>193.77</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>1</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>69.47</td>\n",
              "      <td>26</td>\n",
              "      <td>59785.94</td>\n",
              "      <td>236.50</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>0</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>74.15</td>\n",
              "      <td>29</td>\n",
              "      <td>54806.18</td>\n",
              "      <td>245.89</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>1</td>\n",
              "      <td>Italy</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>68.37</td>\n",
              "      <td>35</td>\n",
              "      <td>73889.99</td>\n",
              "      <td>225.58</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>0</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Daily Time Spent on Site  Age  ...            Timestamp  Clicked on Ad\n",
              "0                     68.95   35  ...  2016-03-27 00:53:11              0\n",
              "1                     80.23   31  ...  2016-04-04 01:39:02              0\n",
              "2                     69.47   26  ...  2016-03-13 20:35:42              0\n",
              "3                     74.15   29  ...  2016-01-10 02:31:19              0\n",
              "4                     68.37   35  ...  2016-06-03 03:36:18              0\n",
              "\n",
              "[5 rows x 10 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CxrvlAxphfMB",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "905e1914-af8f-4249-9c81-5fd00664977e"
      },
      "source": [
        "# Возвратим последние 5 строк загруженного датафрейма\n",
        "df.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>72.97</td>\n",
              "      <td>30</td>\n",
              "      <td>71384.57</td>\n",
              "      <td>208.58</td>\n",
              "      <td>Fundamental modular algorithm</td>\n",
              "      <td>Duffystad</td>\n",
              "      <td>1</td>\n",
              "      <td>Lebanon</td>\n",
              "      <td>2016-02-11 21:49:00</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>51.30</td>\n",
              "      <td>45</td>\n",
              "      <td>67782.17</td>\n",
              "      <td>134.42</td>\n",
              "      <td>Grass-roots cohesive monitoring</td>\n",
              "      <td>New Darlene</td>\n",
              "      <td>1</td>\n",
              "      <td>Bosnia and Herzegovina</td>\n",
              "      <td>2016-04-22 02:07:01</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>51.63</td>\n",
              "      <td>51</td>\n",
              "      <td>42415.72</td>\n",
              "      <td>120.37</td>\n",
              "      <td>Expanded intangible solution</td>\n",
              "      <td>South Jessica</td>\n",
              "      <td>1</td>\n",
              "      <td>Mongolia</td>\n",
              "      <td>2016-02-01 17:24:57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>55.55</td>\n",
              "      <td>19</td>\n",
              "      <td>41920.79</td>\n",
              "      <td>187.95</td>\n",
              "      <td>Proactive bandwidth-monitored policy</td>\n",
              "      <td>West Steven</td>\n",
              "      <td>0</td>\n",
              "      <td>Guatemala</td>\n",
              "      <td>2016-03-24 02:35:54</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>45.01</td>\n",
              "      <td>26</td>\n",
              "      <td>29875.80</td>\n",
              "      <td>178.35</td>\n",
              "      <td>Virtual 5thgeneration emulation</td>\n",
              "      <td>Ronniemouth</td>\n",
              "      <td>0</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>2016-06-03 21:43:21</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     Daily Time Spent on Site  Age  ...            Timestamp  Clicked on Ad\n",
              "995                     72.97   30  ...  2016-02-11 21:49:00              1\n",
              "996                     51.30   45  ...  2016-04-22 02:07:01              1\n",
              "997                     51.63   51  ...  2016-02-01 17:24:57              1\n",
              "998                     55.55   19  ...  2016-03-24 02:35:54              0\n",
              "999                     45.01   26  ...  2016-06-03 21:43:21              1\n",
              "\n",
              "[5 rows x 10 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "N-Rg0oBe1cux"
      },
      "source": [
        "# Статистика датасета"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V-CglBKUdvmT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c0fd2f73-db47-4c70-b5f1-ff272aa2018b"
      },
      "source": [
        "# Посмотрим количество строк в датафрейме\n",
        "len(df)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I2jKJhF2XAev",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cd44b6a6-0c7b-49d0-a92e-766d522bcd69"
      },
      "source": [
        "# Посмотрим количество строк и столбцов в датафрейме\n",
        "df.shape"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1000, 10)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1U-HdgE8q7Bp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "510c815b-a804-4831-9fa4-21ac48bb23e1"
      },
      "source": [
        "# Общая статистика датасета\n",
        "df.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1000 entries, 0 to 999\n",
            "Data columns (total 10 columns):\n",
            " #   Column                    Non-Null Count  Dtype  \n",
            "---  ------                    --------------  -----  \n",
            " 0   Daily Time Spent on Site  1000 non-null   float64\n",
            " 1   Age                       1000 non-null   int64  \n",
            " 2   Area Income               1000 non-null   float64\n",
            " 3   Daily Internet Usage      1000 non-null   float64\n",
            " 4   Ad Topic Line             1000 non-null   object \n",
            " 5   City                      1000 non-null   object \n",
            " 6   Male                      1000 non-null   int64  \n",
            " 7   Country                   1000 non-null   object \n",
            " 8   Timestamp                 1000 non-null   object \n",
            " 9   Clicked on Ad             1000 non-null   int64  \n",
            "dtypes: float64(3), int64(3), object(4)\n",
            "memory usage: 78.2+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hd_aynbhq-rD",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "267e3597-5d2d-456d-eb66-ef7dbfa700eb"
      },
      "source": [
        "# Описательная статистика для числовых столбцов датасета\n",
        "df.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Male</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>65.000200</td>\n",
              "      <td>36.009000</td>\n",
              "      <td>55000.000080</td>\n",
              "      <td>180.000100</td>\n",
              "      <td>0.481000</td>\n",
              "      <td>0.50000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>15.853615</td>\n",
              "      <td>8.785562</td>\n",
              "      <td>13414.634022</td>\n",
              "      <td>43.902339</td>\n",
              "      <td>0.499889</td>\n",
              "      <td>0.50025</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>32.600000</td>\n",
              "      <td>19.000000</td>\n",
              "      <td>13996.500000</td>\n",
              "      <td>104.780000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>51.360000</td>\n",
              "      <td>29.000000</td>\n",
              "      <td>47031.802500</td>\n",
              "      <td>138.830000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>68.215000</td>\n",
              "      <td>35.000000</td>\n",
              "      <td>57012.300000</td>\n",
              "      <td>183.130000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.50000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>78.547500</td>\n",
              "      <td>42.000000</td>\n",
              "      <td>65470.635000</td>\n",
              "      <td>218.792500</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>91.430000</td>\n",
              "      <td>61.000000</td>\n",
              "      <td>79484.800000</td>\n",
              "      <td>269.960000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.00000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       Daily Time Spent on Site          Age  ...         Male  Clicked on Ad\n",
              "count               1000.000000  1000.000000  ...  1000.000000     1000.00000\n",
              "mean                  65.000200    36.009000  ...     0.481000        0.50000\n",
              "std                   15.853615     8.785562  ...     0.499889        0.50025\n",
              "min                   32.600000    19.000000  ...     0.000000        0.00000\n",
              "25%                   51.360000    29.000000  ...     0.000000        0.00000\n",
              "50%                   68.215000    35.000000  ...     0.000000        0.50000\n",
              "75%                   78.547500    42.000000  ...     1.000000        1.00000\n",
              "max                   91.430000    61.000000  ...     1.000000        1.00000\n",
              "\n",
              "[8 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nreFr6pcslNm",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 164
        },
        "outputId": "47c75dff-4f9f-45b5-ee03-a20887457072"
      },
      "source": [
        "# Описательная статистика для нечисловых столбцов датасета\n",
        "df.describe(include=['object', 'bool'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>unique</th>\n",
              "      <td>1000</td>\n",
              "      <td>969</td>\n",
              "      <td>237</td>\n",
              "      <td>1000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>top</th>\n",
              "      <td>Vision-oriented multi-tasking success</td>\n",
              "      <td>Williamsport</td>\n",
              "      <td>Czech Republic</td>\n",
              "      <td>2016-06-05 07:54:30</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>freq</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>9</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                Ad Topic Line  ...            Timestamp\n",
              "count                                    1000  ...                 1000\n",
              "unique                                   1000  ...                 1000\n",
              "top     Vision-oriented multi-tasking success  ...  2016-06-05 07:54:30\n",
              "freq                                        1  ...                    1\n",
              "\n",
              "[4 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ygk7IDCstbKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "10c07fcf-5970-41b9-d167-5dfa0d1c7620"
      },
      "source": [
        "# Подсчет встречаемости категорий в частотах\n",
        "df['Clicked on Ad'].value_counts()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    500\n",
              "0    500\n",
              "Name: Clicked on Ad, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uMieHKJYu0ut",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "670f68b3-7f0c-404b-cff5-0db3a9890e04"
      },
      "source": [
        "# Подсчет встречаемости категорий в долях\n",
        "df['Country'].value_counts(normalize = True).head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Czech Republic    0.009\n",
              "France            0.009\n",
              "Australia         0.008\n",
              "Afghanistan       0.008\n",
              "Cyprus            0.008\n",
              "Name: Country, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0427_kvNvTxG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "998e3eb1-4ba1-4dc4-9963-f93899b2943e"
      },
      "source": [
        "# Подсчет числа уникальных значений столбца\n",
        "df['City'].nunique()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "969"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f1XTG33iwaFR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d263f1f8-07eb-478d-b8f6-ad65faff4897"
      },
      "source": [
        "# Вывод на экран всех уникальных значений столбца\n",
        "df['City'].unique()[:10]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Wrightburgh', 'West Jodi', 'Davidton', 'West Terrifurt',\n",
              "       'South Manuel', 'Jamieberg', 'Brandonstad', 'Port Jefferybury',\n",
              "       'West Colin', 'Ramirezton'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-wx5kjkmz0sK"
      },
      "source": [
        "# Извлечение данных"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WHZHIe2j1l5Z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f4b129b2-0be7-43db-d755-d5d9f0dfdb97"
      },
      "source": [
        "# Извлечение отдельного столбца\n",
        "df['Daily Time Spent on Site']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      68.95\n",
              "1      80.23\n",
              "2      69.47\n",
              "3      74.15\n",
              "4      68.37\n",
              "       ...  \n",
              "995    72.97\n",
              "996    51.30\n",
              "997    51.63\n",
              "998    55.55\n",
              "999    45.01\n",
              "Name: Daily Time Spent on Site, Length: 1000, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2FnYcfvD2JTU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1cc50595-2dc0-4aee-818e-066fc00bebed"
      },
      "source": [
        "# Другой способ (но лучше не прибегать к нему)\n",
        "df.Age"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      35\n",
              "1      31\n",
              "2      26\n",
              "3      29\n",
              "4      35\n",
              "       ..\n",
              "995    30\n",
              "996    45\n",
              "997    51\n",
              "998    19\n",
              "999    26\n",
              "Name: Age, Length: 1000, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IXZzkFlg2hkg",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "outputId": "792c1a84-9d6a-40d2-ae3f-894df137b47e"
      },
      "source": [
        "# Извлечение нескольких столбцов\n",
        "df[['Country', 'City', 'Area Income']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>Lebanon</td>\n",
              "      <td>Duffystad</td>\n",
              "      <td>71384.57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>Bosnia and Herzegovina</td>\n",
              "      <td>New Darlene</td>\n",
              "      <td>67782.17</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>Mongolia</td>\n",
              "      <td>South Jessica</td>\n",
              "      <td>42415.72</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>Guatemala</td>\n",
              "      <td>West Steven</td>\n",
              "      <td>41920.79</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>Ronniemouth</td>\n",
              "      <td>29875.80</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1000 rows × 3 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                    Country            City  Area Income\n",
              "0                   Tunisia     Wrightburgh     61833.90\n",
              "1                     Nauru       West Jodi     68441.85\n",
              "2                San Marino        Davidton     59785.94\n",
              "3                     Italy  West Terrifurt     54806.18\n",
              "4                   Iceland    South Manuel     73889.99\n",
              "..                      ...             ...          ...\n",
              "995                 Lebanon       Duffystad     71384.57\n",
              "996  Bosnia and Herzegovina     New Darlene     67782.17\n",
              "997                Mongolia   South Jessica     42415.72\n",
              "998               Guatemala     West Steven     41920.79\n",
              "999                  Brazil     Ronniemouth     29875.80\n",
              "\n",
              "[1000 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fREvI9rM3F4H",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1fd10865-c135-4efa-d03e-b851880e479a"
      },
      "source": [
        "# Добавление новых столбцов\n",
        "df['Site time share'] = df['Daily Time Spent on Site'] / df['Daily Internet Usage']\n",
        "df['Site time share'].head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    0.269241\n",
              "1    0.414048\n",
              "2    0.293742\n",
              "3    0.301558\n",
              "4    0.303085\n",
              "Name: Site time share, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W-dHbEFN5YfS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "00cf86fd-c912-4ce5-9b93-d58ba2d303de"
      },
      "source": [
        "# Применение статистических методов к столбцам (группам столбцов), например, вычисление среднего:\n",
        "df[['Daily Time Spent on Site', 'Daily Internet Usage', 'Age']].mean()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Daily Time Spent on Site     65.0002\n",
              "Daily Internet Usage        180.0001\n",
              "Age                          36.0090\n",
              "dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2eQMOKrc4a4V"
      },
      "source": [
        "# Фильтрация данных"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T1lUm2MS4eNA",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "0c88f5fe-ece0-42dc-92ce-368f4ab56516"
      },
      "source": [
        "# Фильтрация данных встроенными способами\n",
        "filtered_age = df[df['Age'] > 35]\n",
        "filtered_age.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>66.00</td>\n",
              "      <td>48</td>\n",
              "      <td>24593.33</td>\n",
              "      <td>131.76</td>\n",
              "      <td>Reactive local challenge</td>\n",
              "      <td>Port Jefferybury</td>\n",
              "      <td>1</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-03-07 01:40:15</td>\n",
              "      <td>1</td>\n",
              "      <td>0.500911</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>47.64</td>\n",
              "      <td>49</td>\n",
              "      <td>45632.51</td>\n",
              "      <td>122.02</td>\n",
              "      <td>Centralized neutral neural-net</td>\n",
              "      <td>West Brandonton</td>\n",
              "      <td>0</td>\n",
              "      <td>Qatar</td>\n",
              "      <td>2016-03-16 20:19:01</td>\n",
              "      <td>1</td>\n",
              "      <td>0.390428</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>83.07</td>\n",
              "      <td>37</td>\n",
              "      <td>62491.01</td>\n",
              "      <td>230.87</td>\n",
              "      <td>Team-oriented grid-enabled Local Area Network</td>\n",
              "      <td>East Theresashire</td>\n",
              "      <td>1</td>\n",
              "      <td>Burundi</td>\n",
              "      <td>2016-05-08 08:10:10</td>\n",
              "      <td>0</td>\n",
              "      <td>0.359813</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>69.57</td>\n",
              "      <td>48</td>\n",
              "      <td>51636.92</td>\n",
              "      <td>113.12</td>\n",
              "      <td>Centralized content-based focus group</td>\n",
              "      <td>West Katiefurt</td>\n",
              "      <td>1</td>\n",
              "      <td>Egypt</td>\n",
              "      <td>2016-06-03 01:14:41</td>\n",
              "      <td>1</td>\n",
              "      <td>0.615011</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>55.39</td>\n",
              "      <td>37</td>\n",
              "      <td>23936.86</td>\n",
              "      <td>129.41</td>\n",
              "      <td>Customizable multi-tasking website</td>\n",
              "      <td>West Dylanberg</td>\n",
              "      <td>0</td>\n",
              "      <td>Palestinian Territory</td>\n",
              "      <td>2016-01-30 19:20:41</td>\n",
              "      <td>1</td>\n",
              "      <td>0.428019</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "7                      66.00   48  ...              1         0.500911\n",
              "10                     47.64   49  ...              1         0.390428\n",
              "11                     83.07   37  ...              0         0.359813\n",
              "12                     69.57   48  ...              1         0.615011\n",
              "16                     55.39   37  ...              1         0.428019\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vExjk3Ce4cHZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "3283bf9f-dd46-43a5-abfd-1c702607a22c"
      },
      "source": [
        "# Фильтрация данных с использованием нескольких условий\n",
        "filtered_age_country = df[(df['Age'] > 35) & (df['Country'] == 'Australia')]\n",
        "filtered_age_country.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>66.00</td>\n",
              "      <td>48</td>\n",
              "      <td>24593.33</td>\n",
              "      <td>131.76</td>\n",
              "      <td>Reactive local challenge</td>\n",
              "      <td>Port Jefferybury</td>\n",
              "      <td>1</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-03-07 01:40:15</td>\n",
              "      <td>1</td>\n",
              "      <td>0.500911</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>208</th>\n",
              "      <td>59.51</td>\n",
              "      <td>58</td>\n",
              "      <td>39132.64</td>\n",
              "      <td>140.83</td>\n",
              "      <td>Assimilated fault-tolerant hub</td>\n",
              "      <td>Penatown</td>\n",
              "      <td>0</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-06-16 02:01:24</td>\n",
              "      <td>1</td>\n",
              "      <td>0.422566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>470</th>\n",
              "      <td>43.84</td>\n",
              "      <td>36</td>\n",
              "      <td>70592.81</td>\n",
              "      <td>167.42</td>\n",
              "      <td>Public-key real-time definition</td>\n",
              "      <td>Port Jessica</td>\n",
              "      <td>0</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-06-28 09:19:06</td>\n",
              "      <td>1</td>\n",
              "      <td>0.261856</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>500</th>\n",
              "      <td>51.56</td>\n",
              "      <td>46</td>\n",
              "      <td>63102.19</td>\n",
              "      <td>124.85</td>\n",
              "      <td>Business-focused client-driven forecast</td>\n",
              "      <td>Helenborough</td>\n",
              "      <td>0</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-01-07 13:58:51</td>\n",
              "      <td>1</td>\n",
              "      <td>0.412976</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>552</th>\n",
              "      <td>56.39</td>\n",
              "      <td>58</td>\n",
              "      <td>32252.38</td>\n",
              "      <td>154.23</td>\n",
              "      <td>Programmable uniform website</td>\n",
              "      <td>West Shannon</td>\n",
              "      <td>0</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-02-14 10:06:49</td>\n",
              "      <td>1</td>\n",
              "      <td>0.365623</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "7                       66.00   48  ...              1         0.500911\n",
              "208                     59.51   58  ...              1         0.422566\n",
              "470                     43.84   36  ...              1         0.261856\n",
              "500                     51.56   46  ...              1         0.412976\n",
              "552                     56.39   58  ...              1         0.365623\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jCy4Be6Q7IXO",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 223
        },
        "outputId": "7081153c-d1a6-4fb1-a5df-7d4127885456"
      },
      "source": [
        "# Фильтрация данных с помощью метода .loc\n",
        "df.loc[100:105,['Country', 'Area Income']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>100</th>\n",
              "      <td>Western Sahara</td>\n",
              "      <td>31947.65</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>101</th>\n",
              "      <td>Serbia</td>\n",
              "      <td>51864.77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>102</th>\n",
              "      <td>Maldives</td>\n",
              "      <td>59593.56</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>103</th>\n",
              "      <td>Czech Republic</td>\n",
              "      <td>48376.14</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>104</th>\n",
              "      <td>Guernsey</td>\n",
              "      <td>56884.74</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>105</th>\n",
              "      <td>Tanzania</td>\n",
              "      <td>67186.54</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Country  Area Income\n",
              "100  Western Sahara     31947.65\n",
              "101          Serbia     51864.77\n",
              "102        Maldives     59593.56\n",
              "103  Czech Republic     48376.14\n",
              "104        Guernsey     56884.74\n",
              "105        Tanzania     67186.54"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6wChUa8e9ib7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 585
        },
        "outputId": "6efb11d6-c995-4f85-d25f-d36af7c1bfb1"
      },
      "source": [
        "# Фильтрация датасета по значению столбца с помощью метода .loc\n",
        "df.loc[df['Clicked on Ad'] == 1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>66.00</td>\n",
              "      <td>48</td>\n",
              "      <td>24593.33</td>\n",
              "      <td>131.76</td>\n",
              "      <td>Reactive local challenge</td>\n",
              "      <td>Port Jefferybury</td>\n",
              "      <td>1</td>\n",
              "      <td>Australia</td>\n",
              "      <td>2016-03-07 01:40:15</td>\n",
              "      <td>1</td>\n",
              "      <td>0.500911</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>47.64</td>\n",
              "      <td>49</td>\n",
              "      <td>45632.51</td>\n",
              "      <td>122.02</td>\n",
              "      <td>Centralized neutral neural-net</td>\n",
              "      <td>West Brandonton</td>\n",
              "      <td>0</td>\n",
              "      <td>Qatar</td>\n",
              "      <td>2016-03-16 20:19:01</td>\n",
              "      <td>1</td>\n",
              "      <td>0.390428</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>69.57</td>\n",
              "      <td>48</td>\n",
              "      <td>51636.92</td>\n",
              "      <td>113.12</td>\n",
              "      <td>Centralized content-based focus group</td>\n",
              "      <td>West Katiefurt</td>\n",
              "      <td>1</td>\n",
              "      <td>Egypt</td>\n",
              "      <td>2016-06-03 01:14:41</td>\n",
              "      <td>1</td>\n",
              "      <td>0.615011</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>42.95</td>\n",
              "      <td>33</td>\n",
              "      <td>30976.00</td>\n",
              "      <td>143.56</td>\n",
              "      <td>Grass-roots coherent extranet</td>\n",
              "      <td>West William</td>\n",
              "      <td>0</td>\n",
              "      <td>Barbados</td>\n",
              "      <td>2016-03-24 09:31:49</td>\n",
              "      <td>1</td>\n",
              "      <td>0.299178</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>63.45</td>\n",
              "      <td>23</td>\n",
              "      <td>52182.23</td>\n",
              "      <td>140.64</td>\n",
              "      <td>Persistent demand-driven interface</td>\n",
              "      <td>New Travistown</td>\n",
              "      <td>1</td>\n",
              "      <td>Spain</td>\n",
              "      <td>2016-03-09 03:41:30</td>\n",
              "      <td>1</td>\n",
              "      <td>0.451152</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>994</th>\n",
              "      <td>43.70</td>\n",
              "      <td>28</td>\n",
              "      <td>63126.96</td>\n",
              "      <td>173.01</td>\n",
              "      <td>Front-line bifurcated ability</td>\n",
              "      <td>Nicholasland</td>\n",
              "      <td>0</td>\n",
              "      <td>Mayotte</td>\n",
              "      <td>2016-04-04 03:57:48</td>\n",
              "      <td>1</td>\n",
              "      <td>0.252587</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>72.97</td>\n",
              "      <td>30</td>\n",
              "      <td>71384.57</td>\n",
              "      <td>208.58</td>\n",
              "      <td>Fundamental modular algorithm</td>\n",
              "      <td>Duffystad</td>\n",
              "      <td>1</td>\n",
              "      <td>Lebanon</td>\n",
              "      <td>2016-02-11 21:49:00</td>\n",
              "      <td>1</td>\n",
              "      <td>0.349842</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>51.30</td>\n",
              "      <td>45</td>\n",
              "      <td>67782.17</td>\n",
              "      <td>134.42</td>\n",
              "      <td>Grass-roots cohesive monitoring</td>\n",
              "      <td>New Darlene</td>\n",
              "      <td>1</td>\n",
              "      <td>Bosnia and Herzegovina</td>\n",
              "      <td>2016-04-22 02:07:01</td>\n",
              "      <td>1</td>\n",
              "      <td>0.381640</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>51.63</td>\n",
              "      <td>51</td>\n",
              "      <td>42415.72</td>\n",
              "      <td>120.37</td>\n",
              "      <td>Expanded intangible solution</td>\n",
              "      <td>South Jessica</td>\n",
              "      <td>1</td>\n",
              "      <td>Mongolia</td>\n",
              "      <td>2016-02-01 17:24:57</td>\n",
              "      <td>1</td>\n",
              "      <td>0.428927</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>45.01</td>\n",
              "      <td>26</td>\n",
              "      <td>29875.80</td>\n",
              "      <td>178.35</td>\n",
              "      <td>Virtual 5thgeneration emulation</td>\n",
              "      <td>Ronniemouth</td>\n",
              "      <td>0</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>2016-06-03 21:43:21</td>\n",
              "      <td>1</td>\n",
              "      <td>0.252369</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 11 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "7                       66.00   48  ...              1         0.500911\n",
              "10                      47.64   49  ...              1         0.390428\n",
              "12                      69.57   48  ...              1         0.615011\n",
              "14                      42.95   33  ...              1         0.299178\n",
              "15                      63.45   23  ...              1         0.451152\n",
              "..                        ...  ...  ...            ...              ...\n",
              "994                     43.70   28  ...              1         0.252587\n",
              "995                     72.97   30  ...              1         0.349842\n",
              "996                     51.30   45  ...              1         0.381640\n",
              "997                     51.63   51  ...              1         0.428927\n",
              "999                     45.01   26  ...              1         0.252369\n",
              "\n",
              "[500 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yRZ40qaZD99f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c31898f8-2f6d-4d64-d7f0-e2e6118691b6"
      },
      "source": [
        "# Получение значений столбца для определенного фильтра\n",
        "df.loc[df['Clicked on Ad'] == 1, 'Age']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "7      48\n",
              "10     49\n",
              "12     48\n",
              "14     33\n",
              "15     23\n",
              "       ..\n",
              "994    28\n",
              "995    30\n",
              "996    45\n",
              "997    51\n",
              "999    26\n",
              "Name: Age, Length: 500, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nqtNXlsjEwKF",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "outputId": "61594fec-9752-4745-ca1f-930e8d1dfc75"
      },
      "source": [
        "# Фильтрация данных с помощью метода .iloc\n",
        "df.iloc[:,[1, 6]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Male</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>35</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>31</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>26</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>29</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>35</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>30</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>45</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>51</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>19</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>26</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1000 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Age  Male\n",
              "0     35     0\n",
              "1     31     1\n",
              "2     26     0\n",
              "3     29     1\n",
              "4     35     0\n",
              "..   ...   ...\n",
              "995   30     1\n",
              "996   45     1\n",
              "997   51     1\n",
              "998   19     0\n",
              "999   26     0\n",
              "\n",
              "[1000 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QT9G6HrgFD3d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "outputId": "0a4d66a8-3c71-4aa2-d505-f841da41fe38"
      },
      "source": [
        "# Фильтрация данных с помощью метода .filter\n",
        "country_stats = df.filter(items = ['Country', 'Area Income'])\n",
        "country_stats.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Tunisia</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Nauru</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Marino</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Italy</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Iceland</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      Country  Area Income\n",
              "0     Tunisia     61833.90\n",
              "1       Nauru     68441.85\n",
              "2  San Marino     59785.94\n",
              "3       Italy     54806.18\n",
              "4     Iceland     73889.99"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5H18cm6IIJ0S",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "outputId": "1249510d-a96c-48d4-cb6d-c674ad91c1dd"
      },
      "source": [
        "# Фильтрация строк с помощью метода .query\n",
        "country_stats.query('`Area Income` > 50000').head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Tunisia</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Nauru</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Marino</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Italy</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Iceland</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      Country  Area Income\n",
              "0     Tunisia     61833.90\n",
              "1       Nauru     68441.85\n",
              "2  San Marino     59785.94\n",
              "3       Italy     54806.18\n",
              "4     Iceland     73889.99"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JQkiBPFKJHeX",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "22691bdf-25ae-40fb-c81d-81b9b1e68d99"
      },
      "source": [
        "# Фильтрация текстовых стобцов с помощью метода .contains\n",
        "df[df['Country'].str.contains('ru', case = False)].head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>80.23</td>\n",
              "      <td>31</td>\n",
              "      <td>68441.85</td>\n",
              "      <td>193.77</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>1</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>0.414048</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>83.07</td>\n",
              "      <td>37</td>\n",
              "      <td>62491.01</td>\n",
              "      <td>230.87</td>\n",
              "      <td>Team-oriented grid-enabled Local Area Network</td>\n",
              "      <td>East Theresashire</td>\n",
              "      <td>1</td>\n",
              "      <td>Burundi</td>\n",
              "      <td>2016-05-08 08:10:10</td>\n",
              "      <td>0</td>\n",
              "      <td>0.359813</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>74.58</td>\n",
              "      <td>40</td>\n",
              "      <td>23821.72</td>\n",
              "      <td>135.51</td>\n",
              "      <td>Advanced 24/7 productivity</td>\n",
              "      <td>Millertown</td>\n",
              "      <td>1</td>\n",
              "      <td>Russian Federation</td>\n",
              "      <td>2016-02-27 04:43:07</td>\n",
              "      <td>1</td>\n",
              "      <td>0.550365</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>41.49</td>\n",
              "      <td>52</td>\n",
              "      <td>32635.70</td>\n",
              "      <td>164.83</td>\n",
              "      <td>Mandatory disintermediate utilization</td>\n",
              "      <td>South John</td>\n",
              "      <td>0</td>\n",
              "      <td>Burundi</td>\n",
              "      <td>2016-05-20 08:49:33</td>\n",
              "      <td>1</td>\n",
              "      <td>0.251714</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>67.64</td>\n",
              "      <td>35</td>\n",
              "      <td>51473.28</td>\n",
              "      <td>267.01</td>\n",
              "      <td>Programmable asymmetric data-warehouse</td>\n",
              "      <td>Phelpschester</td>\n",
              "      <td>1</td>\n",
              "      <td>Peru</td>\n",
              "      <td>2016-07-02 20:23:15</td>\n",
              "      <td>0</td>\n",
              "      <td>0.253324</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "1                      80.23   31  ...              0         0.414048\n",
              "11                     83.07   37  ...              0         0.359813\n",
              "19                     74.58   40  ...              1         0.550365\n",
              "22                     41.49   52  ...              1         0.251714\n",
              "30                     67.64   35  ...              0         0.253324\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lKfU4551MN5S",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "71a79990-0be6-435e-818b-f9e5d269e14c"
      },
      "source": [
        "df[df['Country'].str.contains('ru|bo|ja', case = False)].tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>973</th>\n",
              "      <td>80.87</td>\n",
              "      <td>28</td>\n",
              "      <td>63528.80</td>\n",
              "      <td>203.30</td>\n",
              "      <td>Ameliorated local workforce</td>\n",
              "      <td>Collinsburgh</td>\n",
              "      <td>0</td>\n",
              "      <td>Uruguay</td>\n",
              "      <td>2016-02-27 20:20:25</td>\n",
              "      <td>0</td>\n",
              "      <td>0.397787</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>974</th>\n",
              "      <td>41.88</td>\n",
              "      <td>40</td>\n",
              "      <td>44217.68</td>\n",
              "      <td>126.11</td>\n",
              "      <td>Streamlined exuding adapter</td>\n",
              "      <td>Port Rachel</td>\n",
              "      <td>1</td>\n",
              "      <td>Cyprus</td>\n",
              "      <td>2016-02-28 23:54:44</td>\n",
              "      <td>1</td>\n",
              "      <td>0.332091</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>978</th>\n",
              "      <td>71.40</td>\n",
              "      <td>30</td>\n",
              "      <td>72188.90</td>\n",
              "      <td>166.31</td>\n",
              "      <td>Integrated 3rdgeneration monitoring</td>\n",
              "      <td>Beckton</td>\n",
              "      <td>0</td>\n",
              "      <td>Japan</td>\n",
              "      <td>2016-05-24 17:07:08</td>\n",
              "      <td>0</td>\n",
              "      <td>0.429319</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>983</th>\n",
              "      <td>82.79</td>\n",
              "      <td>32</td>\n",
              "      <td>54429.17</td>\n",
              "      <td>234.81</td>\n",
              "      <td>Distributed fault-tolerant service-desk</td>\n",
              "      <td>Lake Zacharyfurt</td>\n",
              "      <td>1</td>\n",
              "      <td>Brunei Darussalam</td>\n",
              "      <td>2016-02-24 10:36:43</td>\n",
              "      <td>0</td>\n",
              "      <td>0.352583</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>51.30</td>\n",
              "      <td>45</td>\n",
              "      <td>67782.17</td>\n",
              "      <td>134.42</td>\n",
              "      <td>Grass-roots cohesive monitoring</td>\n",
              "      <td>New Darlene</td>\n",
              "      <td>1</td>\n",
              "      <td>Bosnia and Herzegovina</td>\n",
              "      <td>2016-04-22 02:07:01</td>\n",
              "      <td>1</td>\n",
              "      <td>0.381640</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "973                     80.87   28  ...              0         0.397787\n",
              "974                     41.88   40  ...              1         0.332091\n",
              "978                     71.40   30  ...              0         0.429319\n",
              "983                     82.79   32  ...              0         0.352583\n",
              "996                     51.30   45  ...              1         0.381640\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LewN7gWuNSKI"
      },
      "source": [
        "# Сортировка данных"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Luug4KQNNlDO",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "bd46932e-e72d-427b-a664-bc457e520d1d"
      },
      "source": [
        "# Применим сортировку данных для составления рейтинга ТОП-5 пользователей по ср. тратам времени на Интернет\n",
        "df.sort_values(by = 'Daily Internet Usage', ascending = False).head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Site time share</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>247</th>\n",
              "      <td>57.05</td>\n",
              "      <td>41</td>\n",
              "      <td>50278.89</td>\n",
              "      <td>269.96</td>\n",
              "      <td>Seamless full-range website</td>\n",
              "      <td>Port Erinberg</td>\n",
              "      <td>1</td>\n",
              "      <td>Sierra Leone</td>\n",
              "      <td>2016-01-09 03:45:19</td>\n",
              "      <td>1</td>\n",
              "      <td>0.211328</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>67.64</td>\n",
              "      <td>35</td>\n",
              "      <td>51473.28</td>\n",
              "      <td>267.01</td>\n",
              "      <td>Programmable asymmetric data-warehouse</td>\n",
              "      <td>Phelpschester</td>\n",
              "      <td>1</td>\n",
              "      <td>Peru</td>\n",
              "      <td>2016-07-02 20:23:15</td>\n",
              "      <td>0</td>\n",
              "      <td>0.253324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>848</th>\n",
              "      <td>70.39</td>\n",
              "      <td>32</td>\n",
              "      <td>47357.39</td>\n",
              "      <td>261.52</td>\n",
              "      <td>Phased 5thgeneration open system</td>\n",
              "      <td>Sabrinaview</td>\n",
              "      <td>1</td>\n",
              "      <td>Cayman Islands</td>\n",
              "      <td>2016-07-12 10:56:21</td>\n",
              "      <td>0</td>\n",
              "      <td>0.269157</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>367</th>\n",
              "      <td>77.07</td>\n",
              "      <td>40</td>\n",
              "      <td>44559.43</td>\n",
              "      <td>261.02</td>\n",
              "      <td>Face-to-face analyzing encryption</td>\n",
              "      <td>Stephenborough</td>\n",
              "      <td>0</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2016-03-01 10:01:35</td>\n",
              "      <td>0</td>\n",
              "      <td>0.295265</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>617</th>\n",
              "      <td>68.41</td>\n",
              "      <td>38</td>\n",
              "      <td>61428.18</td>\n",
              "      <td>259.76</td>\n",
              "      <td>Grass-roots empowering paradigm</td>\n",
              "      <td>Christopherchester</td>\n",
              "      <td>0</td>\n",
              "      <td>Guinea-Bissau</td>\n",
              "      <td>2016-04-30 15:27:22</td>\n",
              "      <td>0</td>\n",
              "      <td>0.263358</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     Daily Time Spent on Site  Age  ...  Clicked on Ad  Site time share\n",
              "247                     57.05   41  ...              1         0.211328\n",
              "30                      67.64   35  ...              0         0.253324\n",
              "848                     70.39   32  ...              0         0.269157\n",
              "367                     77.07   40  ...              0         0.295265\n",
              "617                     68.41   38  ...              0         0.263358\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SPeFwWh35MtX"
      },
      "source": [
        "# Небольшой челлендж"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DLAeaKctwSzO"
      },
      "source": [
        "# Задание 1: выясните, в какой группе пользователей среди \"молодежи\" (до 30 лет) или \"пенсионеров\" (больше 60 лет) больше доля кликов на рекламу сайта?"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Rkvv19ywL8nO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8a8e8ce5-e9c7-4233-a486-11c86974ea6d"
      },
      "source": [
        "# Решение:\n",
        "\n",
        "print('В группе молодежи доля кликнувших на рекламу:', df['Clicked on Ad'].loc[df['Age'] > 60].mean() * 100, '%')\n",
        "print('В группе пенсионеров доля кликнувших на рекламу:', df['Clicked on Ad'].loc[df['Age'] < 30].mean() * 100, '%')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "В группе молодежи доля кликнувших на рекламу: 100.0 %\n",
            "В группе пенсионеров доля кликнувших на рекламу: 24.62121212121212 %\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N6cDZXUh71AW"
      },
      "source": [
        "# Задание 2: определите, мужчины или женщины больше времени сидят в интернете?"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rrNPzeArNfiw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "674f6196-0f89-429c-d154-a76c14ef9406"
      },
      "source": [
        "# Решение:\n",
        "\n",
        "print('Мужчины проводят в интернете в среднем', round(df.query('Male == 1')['Daily Internet Usage'].mean(),1), 'минут в день')\n",
        "print('Женщины проводят в интернете в среднем', round(df.query('Male == 0')['Daily Internet Usage'].mean(),1), 'минут в день')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Мужчины проводят в интернете в среднем 181.3 минут в день\n",
            "Женщины проводят в интернете в среднем 178.8 минут в день\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FqMsU-q7N49B"
      },
      "source": [
        "# Задание №3: Определеите ТОП-15 стран по количеству пользоваталей на сайте."
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "60nnwXMbSEjF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1e11cb54-af72-4651-89f2-1053ce8d14c9"
      },
      "source": [
        "df['Country'].value_counts().head(15)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Czech Republic            9\n",
              "France                    9\n",
              "Australia                 8\n",
              "Afghanistan               8\n",
              "Cyprus                    8\n",
              "Peru                      8\n",
              "Liberia                   8\n",
              "Micronesia                8\n",
              "South Africa              8\n",
              "Senegal                   8\n",
              "Turkey                    8\n",
              "Greece                    8\n",
              "Bosnia and Herzegovina    7\n",
              "Burundi                   7\n",
              "Bahamas                   7\n",
              "Name: Country, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7dcGKJPdSNfB"
      },
      "source": [
        "# Объединение датафреймов"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MaJ9rhfXSdVR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "4cf34323-2946-454a-c4cd-9b69cd9c119a"
      },
      "source": [
        "# Предположим, что у нас в датасете есть еще один столбец user_id:\n",
        "import numpy as np\n",
        "\n",
        "df = pd.read_csv('advertising.csv')\n",
        "\n",
        "df['User_id'] = pd.Series(range(1000,2000))\n",
        "\n",
        "new_order = [10,0,1,2,3,4,5,6,7,8,9]\n",
        "df = df[df.columns[new_order]]\n",
        "\n",
        "df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Age</th>\n",
              "      <th>Area Income</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>City</th>\n",
              "      <th>Male</th>\n",
              "      <th>Country</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>35</td>\n",
              "      <td>61833.90</td>\n",
              "      <td>256.09</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>0</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>31</td>\n",
              "      <td>68441.85</td>\n",
              "      <td>193.77</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>1</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>26</td>\n",
              "      <td>59785.94</td>\n",
              "      <td>236.50</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>0</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>29</td>\n",
              "      <td>54806.18</td>\n",
              "      <td>245.89</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>1</td>\n",
              "      <td>Italy</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>35</td>\n",
              "      <td>73889.99</td>\n",
              "      <td>225.58</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>0</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ...            Timestamp  Clicked on Ad\n",
              "0     1000                     68.95  ...  2016-03-27 00:53:11              0\n",
              "1     1001                     80.23  ...  2016-04-04 01:39:02              0\n",
              "2     1002                     69.47  ...  2016-03-13 20:35:42              0\n",
              "3     1003                     74.15  ...  2016-01-10 02:31:19              0\n",
              "4     1004                     68.37  ...  2016-06-03 03:36:18              0\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JKc9yVeaSenR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        },
        "outputId": "2c2f96d0-dc18-435c-db9b-4f04131ee622"
      },
      "source": [
        "# Разделим наш датасет на три разных датасета: сведения о действиях пользователя на сайте, личнные данные и макроэкономические данные\n",
        "cols_1 = ['User_id', 'Daily Time Spent on Site', 'Ad Topic Line', 'Timestamp', 'Clicked on Ad']\n",
        "df_site = df[cols_1]\n",
        "\n",
        "print('Размер датасета df_site:', df_site.shape)\n",
        "df_site.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_site: (1000, 5)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ...            Timestamp Clicked on Ad\n",
              "0     1000                     68.95  ...  2016-03-27 00:53:11             0\n",
              "1     1001                     80.23  ...  2016-04-04 01:39:02             0\n",
              "2     1002                     69.47  ...  2016-03-13 20:35:42             0\n",
              "3     1003                     74.15  ...  2016-01-10 02:31:19             0\n",
              "4     1004                     68.37  ...  2016-06-03 03:36:18             0\n",
              "\n",
              "[5 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ropb5DLqbkAK",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        },
        "outputId": "124945df-846b-42f1-b790-50155e650b68"
      },
      "source": [
        "cols_2 = ['User_id', 'Male', 'Age', 'Country', 'City', 'Daily Internet Usage']\n",
        "df_personal = df[cols_2]\n",
        "\n",
        "print('Размер датасета df_personal:', df_personal.shape)\n",
        "df_personal.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_personal: (1000, 6)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Male  Age     Country            City  Daily Internet Usage\n",
              "0     1000     0   35     Tunisia     Wrightburgh                256.09\n",
              "1     1001     1   31       Nauru       West Jodi                193.77\n",
              "2     1002     0   26  San Marino        Davidton                236.50\n",
              "3     1003     1   29       Italy  West Terrifurt                245.89\n",
              "4     1004     0   35     Iceland    South Manuel                225.58"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1yZHjZWzcFOa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        },
        "outputId": "4850bf89-1e89-46d7-e1ec-168c310318fd"
      },
      "source": [
        "cols_3 = ['Country', 'City','Area Income']\n",
        "\n",
        "df_macro = df[cols_3][:-50]\n",
        "\n",
        "print('Размер датасета df_macro:', df_macro.shape)\n",
        "df_macro.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_macro: (950, 3)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      Country            City  Area Income\n",
              "0     Tunisia     Wrightburgh     61833.90\n",
              "1       Nauru       West Jodi     68441.85\n",
              "2  San Marino        Davidton     59785.94\n",
              "3       Italy  West Terrifurt     54806.18\n",
              "4     Iceland    South Manuel     73889.99"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "inSIrBiXcSiS",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        },
        "outputId": "15d2dfc4-06a4-43e6-d8cf-b7490267ffc2"
      },
      "source": [
        "# Предположим, что мы получили эти три датасета из разных источников и теперь нам нужно их объединить\n",
        "\n",
        "df_2 = pd.merge(df_site, df_personal, on = 'User_id', how = 'left')\n",
        "\n",
        "print('Размер датасета df_2:', df_2.shape)\n",
        "df_2.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_2: (1000, 10)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ...            City Daily Internet Usage\n",
              "0     1000                     68.95  ...     Wrightburgh               256.09\n",
              "1     1001                     80.23  ...       West Jodi               193.77\n",
              "2     1002                     69.47  ...        Davidton               236.50\n",
              "3     1003                     74.15  ...  West Terrifurt               245.89\n",
              "4     1004                     68.37  ...    South Manuel               225.58\n",
              "\n",
              "[5 rows x 10 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X1TaYGHZcXk3"
      },
      "source": [
        "# Задание: объедините датасет df_2 с датасетом df_macro"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VUGAJMBKcrqA",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "outputId": "3cae1135-0f26-4109-e842-37a3c3dba7f2"
      },
      "source": [
        "# Решение:\n",
        "\n",
        "df_3 = df_2.merge(df_macro, left_on = ['Country', 'City'], right_on = ['Country', 'City'], how = 'left')\n",
        "\n",
        "print('Размер датасета df_3:', df_3.shape)\n",
        "df_3.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_3: (1000, 11)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ... Daily Internet Usage Area Income\n",
              "0     1000                     68.95  ...               256.09    61833.90\n",
              "1     1001                     80.23  ...               193.77    68441.85\n",
              "2     1002                     69.47  ...               236.50    59785.94\n",
              "3     1003                     74.15  ...               245.89    54806.18\n",
              "4     1004                     68.37  ...               225.58    73889.99\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x3SugV3tikrM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "896399b4-d0b9-423a-c8fa-f6ed631b8dcb"
      },
      "source": [
        "# Т.к. в датасете macro было меньше данных (n = 950), то часть строк в новом датасете будут пустыми или NaN\n",
        "df_3[df_3.isna() == True]\n",
        "print('Частично пустых строк:', df_3.isna().sum())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Частично пустых строк: User_id                      0\n",
            "Daily Time Spent on Site     0\n",
            "Ad Topic Line                0\n",
            "Timestamp                    0\n",
            "Clicked on Ad                0\n",
            "Male                         0\n",
            "Age                          0\n",
            "Country                      0\n",
            "City                         0\n",
            "Daily Internet Usage         0\n",
            "Area Income                 50\n",
            "dtype: int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LhYjMHJcioJN",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "outputId": "8affb148-1fb7-4c15-a584-a83d6444b237"
      },
      "source": [
        "# Посмотрим сколько бы строк было в объединенном датасете, если бы метод объединения был 'inner':\n",
        "\n",
        "df_4 = df_2.merge(df_macro, on = ['Country', 'City'], how = 'inner')\n",
        "\n",
        "print('Размер датасета df_4:', df_4.shape)\n",
        "df_4.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_4: (950, 11)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ... Daily Internet Usage Area Income\n",
              "0     1000                     68.95  ...               256.09    61833.90\n",
              "1     1001                     80.23  ...               193.77    68441.85\n",
              "2     1002                     69.47  ...               236.50    59785.94\n",
              "3     1003                     74.15  ...               245.89    54806.18\n",
              "4     1004                     68.37  ...               225.58    73889.99\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 99
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WHU5uVSulofy",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "outputId": "c884840a-3c8f-4993-b207-b06874f4b6fb"
      },
      "source": [
        "# Посмотрим сколько бы строк было в объединенном датасете, если бы метод объединения был 'right':\n",
        "\n",
        "df_5 = df_2.merge(df_macro, on = ['Country', 'City'], how = 'right')\n",
        "\n",
        "print('Размер датасета df_5:', df_5.shape)\n",
        "df_5.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_5: (950, 11)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_id</th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "      <th>Area Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "      <td>61833.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1001</td>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "      <td>68441.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1002</td>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "      <td>59785.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1003</td>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "      <td>54806.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1004</td>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "      <td>73889.99</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   User_id  Daily Time Spent on Site  ... Daily Internet Usage Area Income\n",
              "0     1000                     68.95  ...               256.09    61833.90\n",
              "1     1001                     80.23  ...               193.77    68441.85\n",
              "2     1002                     69.47  ...               236.50    59785.94\n",
              "3     1003                     74.15  ...               245.89    54806.18\n",
              "4     1004                     68.37  ...               225.58    73889.99\n",
              "\n",
              "[5 rows x 11 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vFTl3EijmVQs",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 241
        },
        "outputId": "b50972e1-7283-4676-e5c0-1e8d222b52cf"
      },
      "source": [
        "# Объдинение датасетов методом join\n",
        "\n",
        "df_6 = df_site.set_index('User_id')\n",
        "df_7 = df_personal.set_index('User_id')\n",
        "\n",
        "df_8 = df_6.join(df_7, how = 'inner')\n",
        "\n",
        "print('Размер датасета df_8:', df_8.shape)\n",
        "df_8.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Размер датасета df_8: (1000, 9)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Daily Time Spent on Site</th>\n",
              "      <th>Ad Topic Line</th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Clicked on Ad</th>\n",
              "      <th>Male</th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>Daily Internet Usage</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>User_id</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1000</th>\n",
              "      <td>68.95</td>\n",
              "      <td>Cloned 5thgeneration orchestration</td>\n",
              "      <td>2016-03-27 00:53:11</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Tunisia</td>\n",
              "      <td>Wrightburgh</td>\n",
              "      <td>256.09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1001</th>\n",
              "      <td>80.23</td>\n",
              "      <td>Monitored national standardization</td>\n",
              "      <td>2016-04-04 01:39:02</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>31</td>\n",
              "      <td>Nauru</td>\n",
              "      <td>West Jodi</td>\n",
              "      <td>193.77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1002</th>\n",
              "      <td>69.47</td>\n",
              "      <td>Organic bottom-line service-desk</td>\n",
              "      <td>2016-03-13 20:35:42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>26</td>\n",
              "      <td>San Marino</td>\n",
              "      <td>Davidton</td>\n",
              "      <td>236.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1003</th>\n",
              "      <td>74.15</td>\n",
              "      <td>Triple-buffered reciprocal time-frame</td>\n",
              "      <td>2016-01-10 02:31:19</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>Italy</td>\n",
              "      <td>West Terrifurt</td>\n",
              "      <td>245.89</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1004</th>\n",
              "      <td>68.37</td>\n",
              "      <td>Robust logistical utilization</td>\n",
              "      <td>2016-06-03 03:36:18</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>Iceland</td>\n",
              "      <td>South Manuel</td>\n",
              "      <td>225.58</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "         Daily Time Spent on Site  ... Daily Internet Usage\n",
              "User_id                            ...                     \n",
              "1000                        68.95  ...               256.09\n",
              "1001                        80.23  ...               193.77\n",
              "1002                        69.47  ...               236.50\n",
              "1003                        74.15  ...               245.89\n",
              "1004                        68.37  ...               225.58\n",
              "\n",
              "[5 rows x 9 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 106
        }
      ]
    }
  ]
}