{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "46792beb",
   "metadata": {},
   "source": [
    "## 1. Import libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "343464ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn import preprocessing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "779933cb",
   "metadata": {},
   "source": [
    "## 2. Loading datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "425831c2",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.7</td>\n",
       "      <td>drizzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>6.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>8.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>1.7</td>\n",
       "      <td>2.9</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <td>1.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>1.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <td>0.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>0.6</td>\n",
       "      <td>2.6</td>\n",
       "      <td>fog</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-1.0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-2.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows ?? 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind  weather\n",
       "date                                                        \n",
       "2012-01-01            0.0      12.8       5.0   4.7  drizzle\n",
       "2012-01-02           10.9      10.6       2.8   4.5     rain\n",
       "2012-01-03            0.8      11.7       7.2   2.3     rain\n",
       "2012-01-04           20.3      12.2       5.6   4.7     rain\n",
       "2012-01-05            1.3       8.9       2.8   6.1     rain\n",
       "...                   ...       ...       ...   ...      ...\n",
       "2015-12-27            8.6       4.4       1.7   2.9     rain\n",
       "2015-12-28            1.5       5.0       1.7   1.3     rain\n",
       "2015-12-29            0.0       7.2       0.6   2.6      fog\n",
       "2015-12-30            0.0       5.6      -1.0   3.4      sun\n",
       "2015-12-31            0.0       5.6      -2.1   3.5      sun\n",
       "\n",
       "[1461 rows x 5 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"/Users/sonamchoki/Desktop/PRJ303/seattle_weather.csv\", index_col= \"date\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "722565dc",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-06-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>22.8</td>\n",
       "      <td>12.2</td>\n",
       "      <td>2.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-06-02</th>\n",
       "      <td>1.0</td>\n",
       "      <td>20.6</td>\n",
       "      <td>12.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-06-03</th>\n",
       "      <td>0.0</td>\n",
       "      <td>22.2</td>\n",
       "      <td>11.1</td>\n",
       "      <td>2.9</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-06-04</th>\n",
       "      <td>0.0</td>\n",
       "      <td>26.1</td>\n",
       "      <td>12.2</td>\n",
       "      <td>3.4</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-06-05</th>\n",
       "      <td>0.0</td>\n",
       "      <td>26.7</td>\n",
       "      <td>14.4</td>\n",
       "      <td>3.1</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-08-28</th>\n",
       "      <td>5.6</td>\n",
       "      <td>26.7</td>\n",
       "      <td>15.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-08-29</th>\n",
       "      <td>19.3</td>\n",
       "      <td>23.9</td>\n",
       "      <td>18.3</td>\n",
       "      <td>3.0</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-08-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>26.1</td>\n",
       "      <td>16.1</td>\n",
       "      <td>2.9</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-08-31</th>\n",
       "      <td>0.0</td>\n",
       "      <td>27.8</td>\n",
       "      <td>13.9</td>\n",
       "      <td>2.6</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-09-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>27.8</td>\n",
       "      <td>15.6</td>\n",
       "      <td>2.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>93 rows ?? 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind weather\n",
       "date                                                       \n",
       "2013-06-01            0.0      22.8      12.2   2.5     sun\n",
       "2013-06-02            1.0      20.6      12.2   3.1    rain\n",
       "2013-06-03            0.0      22.2      11.1   2.9     sun\n",
       "2013-06-04            0.0      26.1      12.2   3.4     sun\n",
       "2013-06-05            0.0      26.7      14.4   3.1     sun\n",
       "...                   ...       ...       ...   ...     ...\n",
       "2013-08-28            5.6      26.7      15.6   1.3    rain\n",
       "2013-08-29           19.3      23.9      18.3   3.0    rain\n",
       "2013-08-30            0.0      26.1      16.1   2.9     sun\n",
       "2013-08-31            0.0      27.8      13.9   2.6     sun\n",
       "2013-09-01            0.0      27.8      15.6   2.5     sun\n",
       "\n",
       "[93 rows x 5 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"2013-06-01\":\"2013-09-01\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "26c10924",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1461, 5)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0c57b56d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "precipitation    1461\n",
       "temp_max         1461\n",
       "temp_min         1461\n",
       "wind             1461\n",
       "weather          1461\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed89a31b",
   "metadata": {},
   "source": [
    "## 3. Cleaning Datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a368fd46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "precipitation    0\n",
       "temp_max         0\n",
       "temp_min         0\n",
       "wind             0\n",
       "weather          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "22ce531b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "precipitation    float64\n",
       "temp_max         float64\n",
       "temp_min         float64\n",
       "wind             float64\n",
       "weather           object\n",
       "dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "33583361",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.index = pd.to_datetime(df.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1e049d53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04',\n",
       "               '2012-01-05', '2012-01-06', '2012-01-07', '2012-01-08',\n",
       "               '2012-01-09', '2012-01-10',\n",
       "               ...\n",
       "               '2015-12-22', '2015-12-23', '2015-12-24', '2015-12-25',\n",
       "               '2015-12-26', '2015-12-27', '2015-12-28', '2015-12-29',\n",
       "               '2015-12-30', '2015-12-31'],\n",
       "              dtype='datetime64[ns]', name='date', length=1461, freq=None)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f7f76dce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "rain       641\n",
       "sun        640\n",
       "fog        101\n",
       "drizzle     53\n",
       "snow        26\n",
       "Name: weather, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['weather'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2288b375",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2014-08-11</th>\n",
       "      <td>0.5</td>\n",
       "      <td>35.6</td>\n",
       "      <td>17.8</td>\n",
       "      <td>2.6</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind weather\n",
       "date                                                       \n",
       "2014-08-11            0.5      35.6      17.8   2.6    rain"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['temp_max'] == df['temp_max'].max()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0f621f04",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-08-04</th>\n",
       "      <td>0.0</td>\n",
       "      <td>33.9</td>\n",
       "      <td>16.7</td>\n",
       "      <td>3.7</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-08-05</th>\n",
       "      <td>0.0</td>\n",
       "      <td>33.9</td>\n",
       "      <td>17.8</td>\n",
       "      <td>1.9</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-08-16</th>\n",
       "      <td>0.0</td>\n",
       "      <td>34.4</td>\n",
       "      <td>18.3</td>\n",
       "      <td>2.8</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-06-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>33.9</td>\n",
       "      <td>17.2</td>\n",
       "      <td>2.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-09-11</th>\n",
       "      <td>0.0</td>\n",
       "      <td>33.9</td>\n",
       "      <td>16.1</td>\n",
       "      <td>2.4</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-07-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>34.4</td>\n",
       "      <td>15.6</td>\n",
       "      <td>3.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-08-11</th>\n",
       "      <td>0.5</td>\n",
       "      <td>35.6</td>\n",
       "      <td>17.8</td>\n",
       "      <td>2.6</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-07-02</th>\n",
       "      <td>0.0</td>\n",
       "      <td>33.9</td>\n",
       "      <td>17.8</td>\n",
       "      <td>3.4</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-07-19</th>\n",
       "      <td>0.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>17.2</td>\n",
       "      <td>3.3</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-07-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>34.4</td>\n",
       "      <td>17.2</td>\n",
       "      <td>3.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-07-31</th>\n",
       "      <td>0.0</td>\n",
       "      <td>34.4</td>\n",
       "      <td>17.8</td>\n",
       "      <td>2.6</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind weather\n",
       "date                                                       \n",
       "2012-08-04            0.0      33.9      16.7   3.7     sun\n",
       "2012-08-05            0.0      33.9      17.8   1.9     sun\n",
       "2012-08-16            0.0      34.4      18.3   2.8     sun\n",
       "2013-06-30            0.0      33.9      17.2   2.5     sun\n",
       "2013-09-11            0.0      33.9      16.1   2.4     sun\n",
       "2014-07-01            0.0      34.4      15.6   3.5     sun\n",
       "2014-08-11            0.5      35.6      17.8   2.6    rain\n",
       "2015-07-02            0.0      33.9      17.8   3.4     sun\n",
       "2015-07-19            0.0      35.0      17.2   3.3     sun\n",
       "2015-07-30            0.0      34.4      17.2   3.5     sun\n",
       "2015-07-31            0.0      34.4      17.8   2.6     sun"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['temp_max'] > 33.5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8957dee5",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2014-02-06</th>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.6</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>4.5</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind weather\n",
       "date                                                       \n",
       "2014-02-06            0.0      -1.6      -6.0   4.5     sun"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['temp_max'] == df['temp_max'].min()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f8bac51",
   "metadata": {},
   "source": [
    "### Label Encoding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3fbf8f6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/sonamchoki/opt/anaconda3/lib/python3.9/site-packages/sklearn/utils/validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    }
   ],
   "source": [
    "ladel_encoding = preprocessing.LabelEncoder()\n",
    "ladel_encoding.fit(df[['weather']])\n",
    "new_y = ladel_encoding.transform(df[['weather']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c49b2ac8",
   "metadata": {},
   "source": [
    "### Label Encoding Map = { 'drizzle' : 0, 'fog' : 1, 'rain' : 2, 'snow' : 3, 'sun' : 4}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cdcc5520",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 2, 2, ..., 1, 4, 4])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e99a9fca",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows ?? 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            weather\n",
       "date               \n",
       "2012-01-01        0\n",
       "2012-01-02        2\n",
       "2012-01-03        2\n",
       "2012-01-04        2\n",
       "2012-01-05        2\n",
       "...             ...\n",
       "2015-12-27        2\n",
       "2015-12-28        2\n",
       "2015-12-29        1\n",
       "2015-12-30        4\n",
       "2015-12-31        4\n",
       "\n",
       "[1461 rows x 1 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_ydf = pd.DataFrame(data=new_y, columns=['weather'], index = df.index)\n",
    "new_ydf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6645930d",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>6.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>8.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>1.7</td>\n",
       "      <td>2.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <td>1.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>1.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <td>0.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>0.6</td>\n",
       "      <td>2.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-1.0</td>\n",
       "      <td>3.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-2.1</td>\n",
       "      <td>3.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows ?? 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind\n",
       "date                                               \n",
       "2012-01-01            0.0      12.8       5.0   4.7\n",
       "2012-01-02           10.9      10.6       2.8   4.5\n",
       "2012-01-03            0.8      11.7       7.2   2.3\n",
       "2012-01-04           20.3      12.2       5.6   4.7\n",
       "2012-01-05            1.3       8.9       2.8   6.1\n",
       "...                   ...       ...       ...   ...\n",
       "2015-12-27            8.6       4.4       1.7   2.9\n",
       "2015-12-28            1.5       5.0       1.7   1.3\n",
       "2015-12-29            0.0       7.2       0.6   2.6\n",
       "2015-12-30            0.0       5.6      -1.0   3.4\n",
       "2015-12-31            0.0       5.6      -2.1   3.5\n",
       "\n",
       "[1461 rows x 4 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[:,:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "40fdcaa1",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>6.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>8.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>1.7</td>\n",
       "      <td>2.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <td>1.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>1.3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <td>0.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>0.6</td>\n",
       "      <td>2.6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-1.0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-2.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows ?? 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind  weather\n",
       "date                                                        \n",
       "2012-01-01            0.0      12.8       5.0   4.7        0\n",
       "2012-01-02           10.9      10.6       2.8   4.5        2\n",
       "2012-01-03            0.8      11.7       7.2   2.3        2\n",
       "2012-01-04           20.3      12.2       5.6   4.7        2\n",
       "2012-01-05            1.3       8.9       2.8   6.1        2\n",
       "...                   ...       ...       ...   ...      ...\n",
       "2015-12-27            8.6       4.4       1.7   2.9        2\n",
       "2015-12-28            1.5       5.0       1.7   1.3        2\n",
       "2015-12-29            0.0       7.2       0.6   2.6        1\n",
       "2015-12-30            0.0       5.6      -1.0   3.4        4\n",
       "2015-12-31            0.0       5.6      -2.1   3.5        4\n",
       "\n",
       "[1461 rows x 5 columns]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df = pd.concat([df.iloc[:,:-1],new_ydf],axis=1)\n",
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "87dddc55",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <td>drizzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <td>fog</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows ?? 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            weather\n",
       "date               \n",
       "2012-01-01  drizzle\n",
       "2012-01-02     rain\n",
       "2012-01-03     rain\n",
       "2012-01-04     rain\n",
       "2012-01-05     rain\n",
       "...             ...\n",
       "2015-12-27     rain\n",
       "2015-12-28     rain\n",
       "2015-12-29      fog\n",
       "2015-12-30      sun\n",
       "2015-12-31      sun\n",
       "\n",
       "[1461 rows x 1 columns]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['weather']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5195c36e",
   "metadata": {},
   "source": [
    "## EDA - Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6170b6e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(new_df.precipitation,bins=20)\n",
    "plt.xlabel(\"precipitation\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4e1ea9ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(new_df.temp_max,bins=20)\n",
    "plt.xlabel(\"Maximum Temperature\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c2cf4d8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(new_df.temp_min,bins=20)\n",
    "plt.xlabel(\"Minimum Temperature\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "cd074348",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(new_df.wind,bins=20)\n",
    "plt.xlabel(\"Wind\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "09cd74c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='date'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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YvTo0XL+/Pmtas+ejgtfmMd3K3fw4iVjOHxfSzVHu8OyZcsYPHjwrm5G2nD77beTm5vLddddt6ub0mzsKd/i/OfmMnt1OS9deiCHDOy0q5uz01By46cAlN57guG8EGKBzrLRgFbL5KWUa4ERFucrgCNbW78NGzZsmGFHM0gddqhhGzaaCauwwkuWLOGCCy4wnMvIyLBl6G0EW1yTOmwiv5vCZmTaF4YNG8bChQt3dTNs7CEIhyWVjX6KczOSF04C26tiN4XNyNiwsefi4WkrGX3XNMpqW69kt4m8DRttiGAozPZar52TtI2wp8rmpy1TTHrL6nytrssm8jZstCG2VDexvdZLnS+YvLANG20Am8jbsNGGCGsMvM3I22gG0jlcbCK/m2IP3aXasJES5F6yaqZDHGUTeRt7Bdp7PPmnn36al156aVc3w8YeCJvI29gr0N6J/B//+EcuvPDCXd0MG3sgbDt5GzsV9827j+WVKQcpTQmDigZxw4GJUxXok4ZMmjSJzp0789Zbb+Hz+TjttNP497//TWlpKccee2wktvuIESO45JJLuO222ygrK4sk+7j99ttZs2YNmzdvZuPGjVx//fVcccUVls+d8/13PHDPXfTq0Y1flyzm9NNPZ9iwYTzyyCM0NTXxwQcf0L9/f0OohMMOO4yxY8cyY8YMqquref7555k4cWJa+2xPgbAFl0lhc/I29grce++99O/fn4ULFzJp0iRWrVrFvHnzWLhwIQsWLOC7774DYPXq1Vx77bUsXryY5cuXR5KGPPDAA9x9992R+hYvXsynn37Kjz/+yB133BE3DLAEVi5byn33P8SSJUt4+eWXWblyJfPmzePyyy/nscces7wvGAwyb948Hn74Yf7973+nvT9stG+k0+TW5uRt7FQk47h3BnZ20pAhI/ana7duZGS44yYNMeP0008H4IADDjA818behXTsVGwib2Ovw85OGuL2eFKqUw+tjNPpjFtmb4btW5Y6bHGNjT0KobDEH4xNdN3ek4bYsNFWsDl5G3sUVpfV4wuGGN6z0HBenzTkuOOOiyQNAcjNzeWVV17B6XSm/BwtaciGDRvSkjTEho22gk3kbexR8AVDca+99tprhuNrr702pszSpUsjv6dMmRL5XVJSYrg2cOBAJk+enLQ94yYcwpADxkeOZ86cGfl92GGHcdhhhwHG8MX6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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "new_df.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "48518ef0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='date'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "new_df[[\"temp_max\",\"temp_min\"]].plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "de82e96d",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>precipitation</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.228555</td>\n",
       "      <td>-0.072684</td>\n",
       "      <td>0.328045</td>\n",
       "      <td>-0.267388</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>temp_max</th>\n",
       "      <td>-0.228555</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.875687</td>\n",
       "      <td>-0.164857</td>\n",
       "      <td>0.322337</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>temp_min</th>\n",
       "      <td>-0.072684</td>\n",
       "      <td>0.875687</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.074185</td>\n",
       "      <td>0.154981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>wind</th>\n",
       "      <td>0.328045</td>\n",
       "      <td>-0.164857</td>\n",
       "      <td>-0.074185</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.065858</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weather</th>\n",
       "      <td>-0.267388</td>\n",
       "      <td>0.322337</td>\n",
       "      <td>0.154981</td>\n",
       "      <td>-0.065858</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               precipitation  temp_max  temp_min      wind   weather\n",
       "precipitation       1.000000 -0.228555 -0.072684  0.328045 -0.267388\n",
       "temp_max           -0.228555  1.000000  0.875687 -0.164857  0.322337\n",
       "temp_min           -0.072684  0.875687  1.000000 -0.074185  0.154981\n",
       "wind                0.328045 -0.164857 -0.074185  1.000000 -0.065858\n",
       "weather            -0.267388  0.322337  0.154981 -0.065858  1.000000"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr = new_df.corr()\n",
    "corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "503edb8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x720 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc={'figure.figsize':(15,10)})\n",
    "sns.heatmap(data= corr,annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a4cbfa5",
   "metadata": {},
   "source": [
    "### Outliners Dectection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a2dfdfca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='precipitation'>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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9KMfxQEHHBDDhw8vveZ7DK2OOuqomDlzZuyxxx6xzz77xJlnnhk33XST9bELauzpAdRj//33j8cff7y0vWbNmtKvd0HEtjWyZs2a0rY1wu9+97uYOnVqXH755dHU1BSPPfaYNUJERPzlL3+JzZs3x2GHHRZvf/vbY+zYsXHfffdFQ0NDaR/rY9d17733xpo1a+K0006LV155JTZs2BAvvPCC9UFERDz++OOxZcuWUmwXi8U48MADfX/ZBfWpT6aOP/74WLx4cbz88suxcePG+OUvfxkjR47s6WHRixxxxBHx3HPPxYoVK6K5uTkWLFhgjezCXnzxxZgyZUrMmjUrmpqaIsIaYbvnn38+rrjiiti8eXNs3rw5HnjggTj77LOtDyIi4rbbbosFCxbEz372s5g6dWqceOKJceutt1ofRETEa6+9FjNnzoxNmzbF66+/Hj/5yU/isssusz52QX3qk6l3vetdcemll8Z5550XW7ZsiTPPPDPe97739fSw6EXe9ra3xXXXXRcXX3xxbNq0KUaNGhUnn3xyTw+LHvLtb387Nm3aFNddd13ptbPPPtsaISIiRo0aFcuWLYvTTz89GhoaYuzYsdHU1BT77LOP9UG7fI+h1ZgxY+KJJ56I008/PVpaWuLcc8+No446yvrYBRWKxWKxpwcBAADQ1/SpX/MDAADoLcQUAABAgpgCAABIEFMAAAAJYgoAACBBTAHQYy644IL485//XHOf2bNnx09/+tOIiJgzZ0786le/6vS85fuVHw8AO1Of+v9MAfDWMm/evE73ueSSS0p/XrJkSRx66KGdHlO+X/nxALAziSkAalqyZEnMmjUrBg8eHM8++2z0798/rrvuupg3b16sW7cuVq1aFaNHj45LLrkkZs2aFUuXLo3m5uY4/PDD44orroiBAwfGc889F1dddVW8/PLL0a9fv5g8eXKMGzcuTjzxxJg9e3Zs2LCh3WsccsghMX369Bg6dGj0798/nnzyyZg5c2Y0NDTEoYceGldffXWsX78+1qxZE+95z3vixhtvjB//+McV+z3wwAMxdOjQ+MxnPhOPP/54zJw5MzZu3Bi77bZbfP7zn4+RI0fG3XffHffff3/069cvVqxYEf37948ZM2bEIYcc0tPTD0Av5tf8AOjUk08+GRMmTIj58+fHGWecEdOmTYuIiDfeeCPuueeemDZtWsydOzcaGhri7rvvjp///Oex3377xaxZsyIi4rLLLouTTz457rnnnpg7d25cf/318frrr3fpGq0++clPxnvf+9744he/GCeddFLcddddcfrpp8ddd90Vv/zlL+P555+PhQsXttmv1dq1a2Pq1Knx5S9/OebPnx8zZsyIadOmxapVqyIiYunSpXHllVfGggUL4ogjjoi5c+d255QC8BbgkykAOvWe97wnjj766IiI+NjHPhZXX3117LfffvGBD3ygtM/ChQvjtddei0WLFkVExJYtW2LfffeNdevWxdNPPx1nnXVWREQccMAB7f57T+1dY+3atR2Oadq0afHoo4/GvHnzYvny5fH3v/89NmzY0OH+y5Yti4MOOiiOOOKIiIgYOnRovP/974/HHnssCoVCDBs2LPbff/+IiDj88MPj/vvvr2eKANgFiSkAOtXQ0NDmtX79+sWAAQNK2y0tLXH55ZfHqFGjIiJi/fr1sWnTpmhs3PatplAolPZ99tlnY/DgwZ1eo73XWl122WXR3Nwcp5xySowePTpefPHFKBaLHe7f3NxcMYaIiGKxGFu3bo3ddtst+vfvX3q9UCjUPBcARPg1PwC64Omnn46nn346IiLuvPPOOOqoo2LPPfes2GfEiBFxxx13xObNm6OlpSWuvPLKuP7662PgwIExbNiw0n9R78UXX4xzzjknXnvttbqv0dDQEFu3bo2IiEceeSSmTJkS48aNi4iIJ554Ipqbm9vs1+rII4+MZ599NpYtWxYREc8880wsXbo0jjnmmB2dHgB2UT6ZAqBT73znO+PGG2+MF154IfbZZ5+YOXNmzJkzp2Kfiy66KGbMmBEf/ehHo7m5OQ477LCYPn16RER8/etfj69+9atx++23R6FQiGuvvTYGDRrU6TWqnXjiiXH99dfHli1b4tJLL40pU6bEgAEDYuDAgfHBD34wVq5c2Wa/Vvvss0/Mnj07rrnmmnjjjTeiUCjE1772tXj3u98dv//973f2lAGwCygU/R4DADUsWbIkrrnmmliwYEGfvgYA7Gx+zQ8AACDBJ1MAAAAJPpkCAABIEFMAAAAJYgoAACBBTAEAACSIKQAAgAQxBQAAkPD/AaJ4yS2fKRuGAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=new_df['precipitation'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9430bb9",
   "metadata": {},
   "source": [
    "### Removing outliners using IQR for precipitation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "56c5052f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.999999999999999 -4.199999999999999\n"
     ]
    }
   ],
   "source": [
    "Q1 = new_df.precipitation.quantile(0.25)\n",
    "Q3 = new_df.precipitation.quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "upperlimit = Q3 + (IQR * 1.5)\n",
    "lowerlimit = Q1 - (IQR * 1.5)\n",
    "print(upperlimit,lowerlimit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5ea6e096",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-17</th>\n",
       "      <td>8.1</td>\n",
       "      <td>3.3</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-18</th>\n",
       "      <td>19.8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-2.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-19</th>\n",
       "      <td>15.2</td>\n",
       "      <td>-1.1</td>\n",
       "      <td>-2.8</td>\n",
       "      <td>1.6</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-12</th>\n",
       "      <td>16.0</td>\n",
       "      <td>8.9</td>\n",
       "      <td>5.6</td>\n",
       "      <td>5.6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-17</th>\n",
       "      <td>21.8</td>\n",
       "      <td>6.7</td>\n",
       "      <td>3.9</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-18</th>\n",
       "      <td>18.5</td>\n",
       "      <td>8.9</td>\n",
       "      <td>4.4</td>\n",
       "      <td>5.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-21</th>\n",
       "      <td>27.4</td>\n",
       "      <td>5.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <td>8.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>1.7</td>\n",
       "      <td>2.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>206 rows ?? 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind  weather\n",
       "date                                                        \n",
       "2012-01-02           10.9      10.6       2.8   4.5        2\n",
       "2012-01-04           20.3      12.2       5.6   4.7        2\n",
       "2012-01-17            8.1       3.3       0.0   5.6        3\n",
       "2012-01-18           19.8       0.0      -2.8   5.0        3\n",
       "2012-01-19           15.2      -1.1      -2.8   1.6        3\n",
       "...                   ...       ...       ...   ...      ...\n",
       "2015-12-12           16.0       8.9       5.6   5.6        2\n",
       "2015-12-17           21.8       6.7       3.9   6.0        2\n",
       "2015-12-18           18.5       8.9       4.4   5.1        2\n",
       "2015-12-21           27.4       5.6       2.8   4.3        2\n",
       "2015-12-27            8.6       4.4       1.7   2.9        2\n",
       "\n",
       "[206 rows x 5 columns]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df[(new_df.precipitation < lowerlimit)  | (new_df.precipitation > upperlimit)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "307eef24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1255, 5)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newdf = new_df[(new_df.precipitation > lowerlimit) & (new_df.precipitation < upperlimit)]\n",
    "newdf.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b1d7f195",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='precipitation'>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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hz70oaJHowOWL18eCxcujCFDhhQ9Ch1UKpVi3bp18fjjj0dTU139tWq/tmHDhrjhhhti/vz50bt37/j85z8fTz75ZAwePLjo0WjH6NGjY/To0RER8fzzz8e4cePiq1/9amHz1NXJ1LJly+LjH/94vPe9740ePXrEpz71qXj44YeLHosOmDdvXtxwww3Rt2/fokehg/r06RMTJ06MAw44IJqbm+OII46IP/3pT0WPRTtOOumk+MEPfhBNTU2xZcuWaG1tjR49ehQ9Fh2wdevWmDlzZlx++eVFj0IV1q5dGxERLS0t8elPfzp++MMfFjwRHbFkyZIYMWJE9OvXL5qbm2PmzJkxaNCgoseiSt/85jdj/Pjx0atXr8JmqKuXUF5++eXo06fPnnXfvn1j9erVBU5ER910001Fj0CVBg4cuOef161bFw899FDcd999BU5ERzU3N8cdd9wR3/3ud+Oss86KQw45pOiR6IDJkyfH+PHjY9OmTUWPQhVee+21OOWUU+L666+PXbt2xaWXXhqHH354nHbaaUWPxjtYv359NDc3x+WXXx6bNm2KIUOGxFVXXVX0WFRh2bJlsWPHjhg+fHihc9TVyVRbW1s0NDTsWZdKpYo1UHvPP/98tLS0xLXXXhv9+/cvehw66Iorrojly5fHpk2bYt68eUWPQzvmz58fhx56aJxyyilFj0KVjjvuuJg+fXoceOCB0atXr7jwwgvjySefLHos2tHa2hrLly+PqVOnxv333x+rV6+OhQsXFj0WVfjRj34UX/jCF4oeo75iql+/frF58+Y9682bN3vbGHSiX//613HZZZfFNddcE+edd17R49ABf/jDH+L3v/99RES85z3viWHDhsVzzz1X8FS052c/+1k89dRTMWrUqLjjjjvisccei6lTpxY9Fh3wzDPPxPLly/esS6WSz07VgYMPPjhOOeWU6NWrV3Tv3j0++clPerdTHdm5c2esXLkyhg4dWvQo9RVTp556aixfvjxeeeWVePPNN+ORRx6J008/veixYJ+0adOmGDduXMyYMSNGjhxZ9Dh00MaNG+O6666LnTt3xs6dO+PRRx+NE044oeixaMfdd98dixcvjp/+9KdxxRVXxNChQ2PSpElFj0UHbNu2LaZPnx5vvfVWbN++PRYuXOgH9dSBM844I5YuXRqvvfZatLa2xi9/+cs45phjih6LDnruueeif//+XeIzwXX10skhhxwS48ePj0svvTR27doVF154YRx77LFFjwX7pO985zvx1ltvxS233LLn1y666KK4+OKLC5yK9gwePDhWr14d5557bjQ2NsawYcPEMHSiM844I1atWhXnnntutLW1xZgxY+K4444reizaMWjQoBg7dmyMGTMmdu3aFaeddlpccMEFRY9FB23YsCH69etX9BgREdFQKpVKRQ8BAABQb+rqbX4AAABdhZgCAABIEFMAAAAJYgoAACBBTAEAACSIKQAK86UvfSleeOGFd7xm9uzZ8ZOf/CQiIubMmRM///nP2933r6/7698PALVUV/+fKQD2LXfeeWe711x55ZV7/nnFihUxYMCAdn/PX1/3178fAGpJTAHwjlasWBEzZsyIww47LNauXRvdu3ePW265Je68887YunVrbNiwIYYMGRJXXnllzJgxI1auXBmtra1x9NFHx3XXXRc9e/aMF198MSZPnhyvvPJKdOvWLb785S/HiBEjYujQoTF79ux44403/u5jHHHEETFx4sQYOHBgdO/ePZ599tmYPn16NDY2xoABA2LKlCnx+uuvx+bNm+PII4+MWbNmxY9//OOK6x599NEYOHBgfPGLX4xnnnkmpk+fHm+++WY0NzfHVVddFaeffnosWLAglixZEt26dYv169dH9+7dY9q0aXHEEUcU/ccPQBfmbX4AtOvZZ5+NSy65JBYtWhTnn39+TJgwISIiduzYEQ8++GBMmDAh5s6dG42NjbFgwYJ44IEHom/fvjFjxoyIiLj66qvjrLPOigcffDDmzp0bt99+e2zfvr1Dj1H22c9+Nj784Q/HtddeG2eeeWbMmzcvzj333Jg3b1488sgjsXHjxnjiiSf+5rqyV199Na644or4xje+EYsWLYpp06bFhAkTYsOGDRERsXLlyrj++utj8eLFMWjQoJg7d25n/pECsA9wMgVAu4488sj42Mc+FhERF1xwQUyZMiX69u0bJ5xwwp5rnnjiidi2bVssW7YsIiJ27doVvXv3jq1bt8aaNWti9OjRERFx6KGH/t3PPf29x3j11VffdqYJEybEU089FXfeeWesW7cuXn755XjjjTfe9vrVq1fHBz7wgRg0aFBERAwcODCOP/74ePrpp6OhoSGOOeaY6NevX0REHH300bFkyZJq/ogA2A+JKQDa1djY+De/1q1bt+jRo8eedVtbW0yaNCkGDx4cERGvv/56vPXWW9HU9P/+U9PQ0LDn2rVr18Zhhx3W7mP8vV8ru/rqq6O1tTWGDx8eQ4YMiU2bNkWpVHrb61tbWytmiIgolUqxe/fuaG5uju7du+/59YaGhnfcCwAivM0PgA5Ys2ZNrFmzJiIi7r///jjuuOPioIMOqrjmE5/4RNx7772xc+fOaGtri+uvvz5uv/326NmzZxxzzDF7fqLepk2b4uKLL45t27ZV/RiNjY2xe/fuiIhYunRpjBs3LkaMGBEREatWrYrW1ta/ua7sox/9aKxduzZWr14dERHPP/98rFy5Mk466aR3+8cDwH7KyRQA7Tr44INj1qxZ8cc//jF69eoV06dPjzlz5lRc85WvfCWmTZsW5513XrS2tsZRRx0VEydOjIiI2267Lb71rW/FPffcEw0NDXHTTTdFnz592n2M/2ro0KFx++23x65du2L8+PExbty46NGjR/Ts2TNOPPHEeOmll/7murJevXrF7Nmz48Ybb4wdO3ZEQ0ND3HzzzXH44YfHb3/721r/kQGwH2goeR8DAO9gxYoVceONN8bixYvr+jEAoNa8zQ8AACDByRQAAECCkykAAIAEMQUAAJAgpgAAABLEFAAAQIKYAgAASBBTAAAACf8XbSnhs496yaAAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=newdf['precipitation'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dd1fee60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='temp_max'>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1MAAAJPCAYAAACZ247IAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAYM0lEQVR4nO3df2zddb3H8XdpyzavZGN3K/5TMf6AJeJkyTQgP+Y2qUhbNgLGQbJBFhQTEIdLuE69EkNccJkSplP8g2CMP4AYF34EFUF+yJiL+GNEg4Q73GDZHJNBx6S2ZT33j6sLdwyhL4FzRh+P/8560vPeefeT02e+p21bo9FoFAAAAGNyWLMHAAAAOBSJKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAh0vNwdnn76bzU66k9RHeg///PN9dRTe5s9Bgewl9ZlN63JXlqTvbQme2lddtOa3gh7OeywtjryyP94yY+/bEyNjjbE1EvwvLQme2lddtOa7KU12UtrspfWZTet6Y2+F2/zAwAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAQEezBwA40A9+8N164omtzR5jXOjsbK+RkX2v6L4DA89UVdXkyVNeu4GoqrHtpVV0dx9d5523pNljALyuxBTQcp54Yms98uj/VPvEKc0ehRfY9/dnqqpq157nmzsILeefXxsA442YAlpS+8Qp9aaj5zd7DF7gua13VVXZCy/yz68NgPHGz0wBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQOCQi6n16++r9evva/YYAADAq+RQ/R6/o9kDjNX9999bVVUnnXRqkycBAABeDYfq9/iH3JUpAACAViCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACHc0eYKwGBp6pgYGB+spXrmzqHJ2d7TUysq+pM/Bi9tK6xrKbxx/fWqP72l/jiYBXy+jzf6/HH9/a9Nfm15rXmNZlN61prK/9kydPfo0nevW5MgUAABA45K5MTZ48pSZPnlL/9V//3dQ5pk8/onbterapM/Bi9tK6xrKbr3zlyvqfJ/76Gk8EvFoO65hYb+2e1vTX5tea15jWZTetaayv/YciV6YAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAh3NHmCsTj55TrNHAAAAXkWH6vf4h1xMnXTSqc0eAQAAeBUdqt/je5sfAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAAQ6mj0AwMHs+/sz9dzWu5o9Bi+w7+/PVFXZCy/yf18b05o9BsDrTkwBLae7++hmjzBudHa218jIvld034GB/3vJmDx5yms4EVVj20trmObcAuOSmAJaznnnLWn2COPG9OlH1K5dzzZ7DA5gLwCHBj8zBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQ6Hi5Oxx2WNvrMcchyXPTmuylddlNa7KX1mQvrcleWpfdtKZDfS8vN39bo9FovE6zAAAAvGF4mx8AAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMjdGtt95aZ5xxRvX09NT3v//9Zo/DCyxevLh6e3trwYIFtWDBgtq0aVOzRxrX9u7dW319fbVt27aqqnrggQeqv7+/enp66uqrr27ydOPXgXtZsWJF9fT07D83P//5z5s84fjzjW98o3p7e6u3t7dWrVpVVc5LqzjYbpyZ5rvmmmvqjDPOqN7e3rr++uuryplpBQfby7g4Lw1esb/85S+NuXPnNp5++unG3/72t0Z/f3/j0UcfbfZYNBqN0dHRxsknn9wYGRlp9ig0Go3f//73jb6+vsa73/3uxhNPPNEYHBxszJkzp/H44483RkZGGkuXLm3cc889zR5z3DlwL41Go9HX19fYuXNnkycbv9avX9/42Mc+1hgaGmoMDw83lixZ0rj11ludlxZwsN3ccccdzkyTbdy4sbFo0aLGyMhIY3BwsDF37tzGww8/7Mw02cH2snnz5nFxXlyZGoMHHnigTjjhhJoyZUq96U1vqg9/+MP105/+tNljUVWPPfZYVVUtXbq0zjzzzPre977X5InGt5tuuqmuuOKK6urqqqqqhx56qI4++ujq7u6ujo6O6u/vd3aa4MC9DA4O1vbt2+tzn/tc9ff315o1a2p0dLTJU44v06dPr89+9rN1+OGHV2dnZ73jHe+oLVu2OC8t4GC72b59uzPTZO9///vru9/9bnV0dNRTTz1V+/btqz179jgzTXawvUycOHFcnBcxNQZPPvlkTZ8+ff/trq6u2rlzZxMn4p/27NlTJ554Yq1du7a+853v1A033FDr169v9ljj1pe//OWaPXv2/tvOTms4cC9//etf64QTTqiVK1fWTTfdVA8++GD96Ec/auKE48+73vWuOv7446uqasuWLfWTn/yk2tranJcWcLDdnHLKKc5MC+js7Kw1a9ZUb29vnXjiiV5jWsSBe3n++efHxXkRU2MwOjpabW1t+283Go3/d5vmmTVrVq1ataqOOOKImjp1ap1zzjl17733Nnss/sHZaU3d3d21du3a6urqqkmTJtXixYudmyZ59NFHa+nSpXX55ZdXd3e389JCXribt7/97c5Mi7j00ktrw4YNtWPHjtqyZYsz0yJeuJcNGzaMi/MipsbgLW95S+3atWv/7V27du1/uwzN9eCDD9aGDRv23240GtXR0dHEiXghZ6c1PfLII/Wzn/1s/23npjl+85vf1AUXXFDLly+vs846y3lpIQfuxplpvs2bN9fDDz9cVVWTJk2qnp6e2rhxozPTZAfby+233z4uzouYGoMPfOADtWHDhtq9e3cNDg7WHXfcUaeeemqzx6Kqnn322Vq1alUNDQ3V3r17a926dXXaaac1eyz+4b3vfW/9+c9/rq1bt9a+ffvqtttuc3ZaQKPRqJUrV9bAwECNjIzUjTfe6Ny8znbs2FEXX3xxrV69unp7e6vKeWkVB9uNM9N827Ztqy984Qs1PDxcw8PDddddd9WiRYucmSY72F7e9773jYvz8sbLw9fQUUcdVZdddlktWbKkRkZG6pxzzqmZM2c2eyyqau7cubVp06ZauHBhjY6O1nnnnVezZs1q9lj8w4QJE+qqq66qT33qUzU0NFRz5syp008/vdljjXszZsyoT3ziE3XuuefW888/Xz09PdXX19fsscaV6667roaGhuqqq67a/2+LFi1yXlrAS+3GmWmuOXPm1EMPPVQLFy6s9vb26unpqd7e3po6daoz00QH28sll1xSRx555Bv+vLQ1Go1Gs4cAAAA41HibHwAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEwZkuXLq3du3c3ewwAaCoxBcCYrV+/vtkjAEDT+aO9AIzJihUrqqrq/PPPr2uvvbZWrlxZO3bsqJGRkert7a1PfvKTtW3btjr//PPrpJNOqj/84Q+1b9++uvTSS+vGG2+sxx57rI477rj62te+Vtu3b6/FixfXKaecUps2bapGo1Ff/OIXa/bs2f9yhnnz5lVfX1/96le/qoGBgbrwwgvrt7/9bf3xj3+sjo6O+ta3vlVHHXVU3X333fXtb3+7hoeHa/fu3bVw4cJatmxZrVu3rtauXVs333xztbW11dlnn10XXXRRLVy48HV4BgF4o/BHewEYs2OPPbY2bNhQy5YtqwsuuKDmzZtXQ0ND9fGPf7wWLVpUM2fOrPnz59c3v/nNmj9/fl1xxRX1y1/+sm655Zbq7Oys+fPn15o1a6qrq6vmz59fq1evrv7+/rr33nvr85//fN19993V2dn5ko8/b968Ou2002rFihV1++231/Lly2vdunU1Y8aMuvjii+s973lPXXTRRbVkyZK68sor621ve1vt3Lmz5s6dW/fff39NnTq1li9fXkcccUQNDw9Xe3t7XXnlla/jMwjAG4ErUwBEBgcH69e//nUNDAzUNddcU1VVzz33XP3pT3+qmTNnVmdnZ82bN6+qqt761rfWrFmz6s1vfnNVVXV1ddXAwEB1dXXV5MmTq7+/v6qq5syZU+3t7fXII4/Ucccd9y8fv6enp6qquru7a9q0aTVjxoz9jzUwMFBtbW117bXX1j333FO33XZbbd68uRqNRg0ODlZV1Ze+9KVasGBBTZw4sX784x+/+k8QAG94YgqASFtbWzUajbrhhhtq0qRJVVW1e/fumjBhQj399NPV2dlZbW1t++//Ulea2tvb/9/t0dHRF/3bwRx++OH/8nM/99xzddZZZ9WHPvShmj17dp199tl155131j/fkPHUU0/V0NBQDQ8P15NPPlnd3d0v/58GgBfwCygAGLP29vbq6Oio448/vq6//vqqqtqzZ0+de+65ddddd43pc+3evbvuu+++qqr6xS9+UZ2dnXXMMcf82zNu3bq19u7dW8uWLat58+bVxo0ba3h4uEZHR2tkZKQ+85nP1Kc//em65JJL6rLLLquRkZF/+zEBGF9cmQJgzE4//fRavHhxff3rX6+vfvWr1d/fX8PDw9XX11dnnnlmbdu27RV/rgkTJtTNN99cq1evrokTJ9batWtf0ZWpl3PsscfWBz/4wfrIRz5Shx9+eB1zzDH1zne+s7Zu3Vo//OEPa9q0afXRj360qqruvPPOuvrqq+vyyy//tx8XgPHDL6AAoGm2bdtW/f399bvf/a7ZowDAmLkyBUDLueWWW+q666476Mf6+/vrwgsvfJ0nAoAXc2UKAAAg4BdQAAAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQOB/AQsyqYyPHFvfAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=new_df['temp_max'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b472f1f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='temp_min'>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1MAAAJPCAYAAACZ247IAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAV6ElEQVR4nO3df2xfdb3H8Xdpy+YuplPZYCYFY4yiIcgiRnBI424s4FZmgBBYMmaW+SMm/oomOuLFX2EIASaaRf/QOK7TwEI2GPgjEiAjbpi4qENMXCC4QTOCw0G3XbbZtd/7B5deQXDste84/c7H47/TfnP2Ts9n53ueOaffdrVarVYBAABwWI5regAAAIBOJKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAg0HOoFzzzzP/U+Lg/RTVZvOlNJ9Tf/ra36TE4xlhXHA3WFUeDdUW7WVP8K8cd11VveMN/vOL3DxlT4+MtMTXJOB4cDdYVR4N1xdFgXdFu1hQpj/kBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAECgp+kBAJg8fvrT/64nntjeln319nbX6OhYW/ZFbmTk2aqq6uub3ugc7WJdVfX3n1oLF17Z9BhAiSkA/sETT2yvrY88Wt1Tpzc9Cm0ytv/Zqqrauftgs4PQFi8cT2ByEFMAvEj31Ok17dT/bHoM2uS57fdWVTmmx4gXjicwOfidKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIdFxMbdz4QG3c+EDTYwAAAG3Sqdf4PU0PcLh+/esNVVU1Z855DU8CAAC0Q6de43fcnSkAAIDJQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAAR6mh7gcI2MPFsjIyN13XXfbHqURvT2dtfo6FjTY3CMsa54weOPb6/xse6mxwBewfjB/fX449v/ba+DjgbvgZPD449vr76+vqbHOGzuTAEAAAQ67s5UX9/06uubXl/60n81PUojZsx4fe3cuafpMTjGWFe84LrrvlmPPvF002MAr+C4nql1Sv+J/7bXQUeD98DJoVPvtrozBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAAB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09HpTj755Nq8efPE9s6dOz0vzhHbvHlzjY6O1jnnnFNVz5+j/O4U7XLyySfXzp07J7adtzhSW7durW3bttX5559fVc5ZHD6P+XWYadOm1Q9+8IOJT8davXq1O1NE3v/+99eDDz5Yu3btqn379tWvfvWrOu+885oeiw63Z8+euv766+vAgQO1d+/eWrdunXMUbfPud7+7/vKXv9T27dtrbGys7r77buctjkir1arly5fXyMhIjY6O1m233eacxWGR3h2mu7u7vv3tb9fXvva12r9/f73lLW+p66+/vumx6EAnnXRSff7zn68rr7yyRkdH69JLL60zzjij6bHocB/84Adry5Yt9ZGPfKTGx8dr4cKFL3rsD47ElClT6lvf+lZ9+tOfrgMHDtTAwEBdcMEFTY9FBzvttNPq4x//eF1xxRV18ODBGhwc9GnJHJauVqvVanoIAACATuMxPwAAgICYAgAACIgpAACAgJgCAAAIiCkAAICAmAIgtmTJktq1a1fTYxzSxz72sXr00UebHgOAY4yPRgcg9o53vKMefPDBeuMb39j0KADwmvNHewGILFu2rKqqFi9eXN///vdr+fLl9eSTT9bo6GjNmzevPvnJT9bw8HAtXry45syZUw8//HCNjY3VZz7zmbrtttvqscceq9NPP71uuumm2rFjRy1atKg+8IEP1JYtW6rVatXVV19dZ5111r+cYe7cuTV//vz6zW9+UyMjI7V06dL63e9+V3/605+qp6envve979VJJ51Uc+fOrZtvvrmee+65WrFiRfX399cjjzxSBw8erK9//ev1nve857X4kQFwjPGYHwCRa6+9tqqqbrnlllq2bFldcskltXbt2rr99ttr06ZN9fOf/7yqqoaHh2tgYKDWrl1bZ555Zl1zzTV100031c9+9rPavHlz/eEPf6iqqh07dtR73/veuvPOO+sLX/hCfe5zn6vR0dFDznHgwIFas2ZNffazn62rr766Fi9eXOvXr69Zs2bVunXr/un1Dz30UC1ZsqTuuOOOuvjii2vFihXt+6EA8G9FTAFwRPbt21e//e1v6+abb64FCxbUZZddVk8++WT9+c9/rqqq3t7emjt3blVVnXLKKTV79uw64YQTasqUKTVz5swaGRmpqqq+vr4aGhqqqqqBgYHq7u6urVu3HvLfHxwcrKqq/v7+OvHEE+u0006b+Lde2Pc/evOb31zvfOc7q6rqXe9618u+BgBeDY/5AXBEurq6qtVq1a233lqve93rqqpq165dNWXKlHrmmWeqt7e3urq6Jl7f29v7svvp7u5+0fb4+Pg/fe3lHH/88Yfc9z+aOnXqP80OAAl3pgCIdXd3V09PT5155pn1ox/9qKqqdu/eXVdccUXde++9h7WvXbt21QMPPFBVVffdd1/19vbW29/+9rbPDADt4s4UALELLrigFi1aVN/97nfrxhtvrKGhofr73/9e8+fPr4suuqiGh4df9b6mTJlSd955Z91www01derUWrly5au6MwUATfHR6AA0bnh4uIaGhur3v/9906MAwKvmzhQAk9b69evrhz/84ct+b2hoqJYuXfoaTwQA/8+dKQAAgIAPoAAAAAiIKQAAgICYAgAACIgpAACAgJgCAAAIiCkAAIDA/wLKmSE4pOByMgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=new_df['temp_min'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e67f3779",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='wind'>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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gJgCAAAIiCkAAICAmAIAAAiIKQAAgICYAgAACIgpAACAwKSmB+yv2bPPanoCANBFPDcAmjLuYmrWrDObngAAdBHPDYCm+JgfAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAAQmNT0Ausngi1tqYMNDTc9o3OCLW6qq3Bej4M/35VFNzwAAxoCYgr94wxtOaHpC19i69c9/NfT1TW12yEHh9XXSSSc1PQIAGANiCv7isssub3oCB6lp015Tmzf/sekZAMAo8zNTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAACBSe2uMGFCT0d/Bt3AY5Nu5bFJt/LYpJt5fNK0do/Bnlar1TpAWwAAAA4aPuYHAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABDoOKbuu+++uuiii+r888+v733ve2O5CfbLbbfdVnPnzq25c+fWl7/85abnwB4WLVpUCxcubHoGDLNixYqaP39+XXjhhXXTTTc1PQeGLF++fOjf9UWLFjU9B15RRzH17LPP1uLFi2vp0qW1bNmyuvvuu+upp54a623Q1po1a2rVqlV1zz331LJly+rxxx+vBx98sOlZMKS/v7/uueeepmfAMJs2baobb7yxbr/99rr33ntr3bp19fDDDzc9C2rbtm31xS9+se66665avnx5rV27ttasWdP0LNinjmJqzZo19Y53vKOmTp1avb29dcEFF9RPfvKTsd4GbU2bNq0WLlxYU6ZMqcmTJ9fJJ59cTz/9dNOzoKqqtmzZUosXL65rrrmm6SkwzIMPPlgXXXRRHX300TV58uRavHhxnXHGGU3PghocHKxdu3bVtm3baufOnbVz58465JBDmp4F+9RRTP3ud7+radOmDV0+8sgj69lnnx2zUdCpU045pd7ylrdUVdX69evrxz/+cZ111lnNjoK/+PznP1/XX399vfa1r216CgyzYcOGGhwcrGuuuabmzZtXS5curb6+vqZnQR122GF13XXX1YUXXlhnnXVWHXfccfXWt7616VmwTx3F1K5du6qnp2focqvVGnYZmvbkk0/WlVdeWZ/+9KfrxBNPbHoO1A9+8IM65phjasaMGU1PgT0MDg5Wf39/3XzzzXX33XfXY4895uOodIXf/OY39cMf/rB+9rOf1cqVK2vChAm1ZMmSpmfBPnUUU0cffXRt3rx56PLmzZvryCOPHLNRsD9++ctf1hVXXFGf+tSn6tJLL216DlRV1QMPPFCrV6+uefPm1a233lorVqyom2++uelZUFVVr3/962vGjBn1ute9rg499NA677zz6rHHHmt6FtSqVatqxowZdcQRR9SUKVNq/vz59fOf/7zpWbBPHcXUzJkzq7+/v37/+9/Xtm3b6qc//WmdeeaZY70N2nrmmWfq2muvra985Ss1d+7cpufAkO985zt1//331/Lly+sTn/hEnXPOOXXDDTc0PQuqqurss8+uVatW1R/+8IcaHByslStX1mmnndb0LKg3vvGNtWbNmhoYGKhWq1UrVqyo6dOnNz0L9mlSJ1c66qij6vrrr6/LL7+8duzYUe9973vr9NNPH+tt0NaSJUtq+/btdcsttwz92YIFC+r9739/g6sAutsZZ5xRV111VV122WW1Y8eOmjVrVr3nPe9pehbU7Nmza926dTV//vyaPHlyTZ8+va6++uqmZ8E+9bRarVbTIwAAAMabjv/TXgAAAP5KTAEAAATEFAAAQEBMAQAABMQUAABAQEwB0DW+9rWv1bJly/bra5YsWVILFy4cm0EA8Ao6+n+mAOBAuO6665qeAAAd884UAAfMvHnzqr+/v6qq7r///po+fXq9+OKLVVX12c9+tmbOnFlLliypqqrp06fX17/+9VqwYEGdc845tXTp0qqq2rFjR9144401Z86cWrBgQf3qV79q5psB4O+emALggJkzZ0498sgjVVW1cuXK6uvrq7Vr11ar1aqHH3643vSmNw1d96WXXqrDDz+8vv/979ett95aX/rSl2r79u21dOnSWr9+ff3oRz+qO++8s5555pmmvh0A/s6JKQAOmN0x1Wq1au3atXXFFVfU6tWr69e//nUdf/zxNW3atGHXP/fcc6uq6rTTTquXXnqpBgYGqr+/vy6++OKaMmVK9fb21iWXXNLEtwIAYgqAA+fUU0+tHTt21EMPPVQnnnhinX322bV69epasWJFXXDBBXtc/5BDDqmqqp6enqqqarVae1xn4sSJYzsaAPZBTAFwQJ133nn11a9+tWbNmlUnn3xyvfDCC3XffffV+eef39HXv/Od76xly5bV9u3ba/v27fXAAw+M8WIA2Du/zQ+AA2rOnDm1ZMmSmjlzZlVVzZw5s5544ok65phjOvr6BQsW1MaNG+viiy+uqVOn1gknnDCWcwFgn3pae/vMBAAAAK/Ix/wAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACDw/6N3oMw8UKmYAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=new_df['wind'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47557b82",
   "metadata": {},
   "source": [
    "### Removing outliners using IQR for wind"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8e945e02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.699999999999999 -0.49999999999999956\n"
     ]
    }
   ],
   "source": [
    "Q1 = new_df.wind.quantile(0.25)\n",
    "Q3 = new_df.wind.quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "upperlimit = Q3 + (IQR * 1.5)\n",
    "lowerlimit = Q1 - (IQR * 1.5)\n",
    "print(upperlimit,lowerlimit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3d853631",
   "metadata": {},
   "outputs": [
    {
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
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-21</th>\n",
       "      <td>3.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>8.2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-02-18</th>\n",
       "      <td>6.4</td>\n",
       "      <td>6.7</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-02-21</th>\n",
       "      <td>0.8</td>\n",
       "      <td>10.0</td>\n",
       "      <td>7.8</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-02-29</th>\n",
       "      <td>0.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.1</td>\n",
       "      <td>7.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-03-03</th>\n",
       "      <td>0.0</td>\n",
       "      <td>12.2</td>\n",
       "      <td>6.7</td>\n",
       "      <td>7.0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-04-01</th>\n",
       "      <td>1.5</td>\n",
       "      <td>8.9</td>\n",
       "      <td>4.4</td>\n",
       "      <td>6.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-04-30</th>\n",
       "      <td>4.3</td>\n",
       "      <td>12.8</td>\n",
       "      <td>7.2</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-10-03</th>\n",
       "      <td>0.0</td>\n",
       "      <td>18.9</td>\n",
       "      <td>7.8</td>\n",
       "      <td>7.3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-12-17</th>\n",
       "      <td>2.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>1.7</td>\n",
       "      <td>9.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-07</th>\n",
       "      <td>2.3</td>\n",
       "      <td>10.0</td>\n",
       "      <td>4.4</td>\n",
       "      <td>7.3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-02-22</th>\n",
       "      <td>9.4</td>\n",
       "      <td>7.8</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-02-25</th>\n",
       "      <td>2.3</td>\n",
       "      <td>10.6</td>\n",
       "      <td>3.3</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-03-20</th>\n",
       "      <td>9.9</td>\n",
       "      <td>11.1</td>\n",
       "      <td>4.4</td>\n",
       "      <td>7.6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-09-29</th>\n",
       "      <td>16.8</td>\n",
       "      <td>14.4</td>\n",
       "      <td>11.1</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-02</th>\n",
       "      <td>12.7</td>\n",
       "      <td>14.4</td>\n",
       "      <td>8.3</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-07</th>\n",
       "      <td>30.0</td>\n",
       "      <td>11.1</td>\n",
       "      <td>10.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-12-01</th>\n",
       "      <td>3.0</td>\n",
       "      <td>13.3</td>\n",
       "      <td>7.8</td>\n",
       "      <td>8.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-01-10</th>\n",
       "      <td>4.3</td>\n",
       "      <td>12.8</td>\n",
       "      <td>8.3</td>\n",
       "      <td>7.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-01-11</th>\n",
       "      <td>21.3</td>\n",
       "      <td>14.4</td>\n",
       "      <td>7.2</td>\n",
       "      <td>8.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-01-12</th>\n",
       "      <td>1.5</td>\n",
       "      <td>11.1</td>\n",
       "      <td>5.6</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-01-13</th>\n",
       "      <td>0.0</td>\n",
       "      <td>10.6</td>\n",
       "      <td>10.0</td>\n",
       "      <td>7.1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-02-16</th>\n",
       "      <td>26.4</td>\n",
       "      <td>9.4</td>\n",
       "      <td>3.9</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-02-20</th>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>6.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-11-06</th>\n",
       "      <td>4.1</td>\n",
       "      <td>16.7</td>\n",
       "      <td>10.6</td>\n",
       "      <td>6.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-11-11</th>\n",
       "      <td>0.0</td>\n",
       "      <td>7.8</td>\n",
       "      <td>1.1</td>\n",
       "      <td>7.7</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-11-12</th>\n",
       "      <td>0.0</td>\n",
       "      <td>6.7</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-12-10</th>\n",
       "      <td>13.0</td>\n",
       "      <td>18.9</td>\n",
       "      <td>10.0</td>\n",
       "      <td>6.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-09-20</th>\n",
       "      <td>4.1</td>\n",
       "      <td>22.8</td>\n",
       "      <td>12.2</td>\n",
       "      <td>6.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-10-30</th>\n",
       "      <td>19.3</td>\n",
       "      <td>17.2</td>\n",
       "      <td>11.7</td>\n",
       "      <td>6.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-10-31</th>\n",
       "      <td>33.0</td>\n",
       "      <td>15.6</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-11-17</th>\n",
       "      <td>29.5</td>\n",
       "      <td>13.3</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-10</th>\n",
       "      <td>9.4</td>\n",
       "      <td>11.7</td>\n",
       "      <td>6.1</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-20</th>\n",
       "      <td>4.3</td>\n",
       "      <td>7.8</td>\n",
       "      <td>4.4</td>\n",
       "      <td>6.7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-23</th>\n",
       "      <td>6.1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.8</td>\n",
       "      <td>7.6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            precipitation  temp_max  temp_min  wind  weather\n",
       "date                                                        \n",
       "2012-01-21            3.0       8.3       3.3   8.2        2\n",
       "2012-02-18            6.4       6.7       3.9   8.1        2\n",
       "2012-02-21            0.8      10.0       7.8   7.5        2\n",
       "2012-02-29            0.8       5.0       1.1   7.0        3\n",
       "2012-03-03            0.0      12.2       6.7   7.0        4\n",
       "2012-04-01            1.5       8.9       4.4   6.8        2\n",
       "2012-04-30            4.3      12.8       7.2   8.0        2\n",
       "2012-10-03            0.0      18.9       7.8   7.3        4\n",
       "2012-12-17            2.0       8.3       1.7   9.5        2\n",
       "2013-01-07            2.3      10.0       4.4   7.3        2\n",
       "2013-02-22            9.4       7.8       3.9   8.1        2\n",
       "2013-02-25            2.3      10.6       3.3   7.1        2\n",
       "2013-03-20            9.9      11.1       4.4   7.6        2\n",
       "2013-09-29           16.8      14.4      11.1   7.1        2\n",
       "2013-11-02           12.7      14.4       8.3   7.9        2\n",
       "2013-11-07           30.0      11.1      10.0   7.2        2\n",
       "2013-12-01            3.0      13.3       7.8   8.8        2\n",
       "2014-01-10            4.3      12.8       8.3   7.0        2\n",
       "2014-01-11           21.3      14.4       7.2   8.8        2\n",
       "2014-01-12            1.5      11.1       5.6   8.1        2\n",
       "2014-01-13            0.0      10.6      10.0   7.1        4\n",
       "2014-02-16           26.4       9.4       3.9   7.9        2\n",
       "2014-02-20            3.0      10.0       5.6   6.9        2\n",
       "2014-11-06            4.1      16.7      10.6   6.7        2\n",
       "2014-11-11            0.0       7.8       1.1   7.7        4\n",
       "2014-11-12            0.0       6.7       0.0   7.6        4\n",
       "2014-12-10           13.0      18.9      10.0   6.7        2\n",
       "2015-09-20            4.1      22.8      12.2   6.8        2\n",
       "2015-10-30           19.3      17.2      11.7   6.7        2\n",
       "2015-10-31           33.0      15.6      11.7   7.2        2\n",
       "2015-11-17           29.5      13.3       6.7   8.0        2\n",
       "2015-12-10            9.4      11.7       6.1   7.5        2\n",
       "2015-12-20            4.3       7.8       4.4   6.7        2\n",
       "2015-12-23            6.1       5.0       2.8   7.6        2"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df[(new_df.wind < lowerlimit)  | (new_df.wind > upperlimit)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "656ae686",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1427, 5)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newdf = new_df[(new_df.wind > lowerlimit) & (new_df.wind < upperlimit)]\n",
    "newdf.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e2d901a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='wind'>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1MAAAJPCAYAAACZ247IAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAVxklEQVR4nO3dW4yddb3G8d8wM4jdm0w5VOWCgxJiDCGEGGW3I5YWpmqnWjxc1EahaRrTbBPUmGijQC9UtI2GUIjZIbZsCCkKF+UkXjQdU+gwoNXY3pgGNT0Q54JNbEs36XQ6XftCyg4Rengyq29n1udzxYJ3Nc/0H6br23ettqvVarUKAACA03JO0wMAAACmIjEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAgZ6TXfCPf/xvHTvmr6Kaii666N/rtdcONT2DM8BZdwbn3Dmcdedw1p3DWU9N55zTVRdc8G/v+t9PGlPHjrXE1BTm7DqHs+4MzrlzOOvO4aw7h7OefrzNDwAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAmIKAAAgIKYAAAACYgoAACAgpgAAAAJiCgAAICCmAAAAAj1NDwDObhs3Plz79u1pesa0c+DA/qqq6uubecrP6e3trvHxifYMoq0uvfTyWrr01qZnADDJxBRwQvv27aldL/+lus+b2fSUaWXi8P6qqnr14NFmh9B2x88agOlHTAEn1X3ezJpx+U1Nz5hW3tizparKz2sHOH7WAEw/PjMFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAIEpF1PDw8/V8PBzTc8AAICO4TX4O+tpesDp2rZta1VV9fd/suElAADQGbwGf2dT7s4UAADA2UBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAAAwqYaGNtfy5Utr69Ytp3T9Sy+9UMuXL63f//7FNi+bXGIKAACYVI888t9VVfXQQxtO6fpf/OK/qqrqgQd+3q5JbSGmAACASTM0tLmqWm8+ap307tRLL71QExNHq6pqYuLolLo71dP0gNN14MD+OnDgQK1Z84Omp5z1enu7a3x8oukZnAHtPOu9e/fUsYnutvzY0AmOHT1ce/fuOa1ft3z/7hzOunNM9bPeu3dP9fX1ndK1x+9KHffQQxtq7tyb3vX643eljnvggZ/Xxz72H6e9sQnuTAEAAJOodZLHb3f8rtS7PT6bTbk7U319M6uvb2Z997t3Nj3lrDdr1vn16quvNz2DM6CdZ71mzQ/qL/v+py0/NnSCc3rOq8suvfi0ft3y/btzOOvOMdXP+vTeFdZVbw+orhNe3d3d87aA6u6eOonizhQAADBpvvKVZW97fNtty094/YoVK9/2+Gtf+8/JntQ2YgoAAJg08+cP1P/fjeo64eelqqquv37OW3ejurt7psznparEFAAAMMmO35062V2p447fnZpKd6WqpuBnpgAAgLPb/PkDb96hOjXXXz+nrr9+ThsXtYc7UwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABDoaXrA6frEJ+Y2PQEAADqK1+DvbMrFVH//J5ueAAAAHcVr8HfmbX4AAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEBBTAAAAATEFAAAQEFMAAAABMQUAABAQUwAAAAExBQAAEOhpegBw9ps4vL/e2LOl6RnTysTh/VVVfl47wD/P+uKmZwDQBmIKOKFLL7286QnT0oED//z229c385Sf09vbXePjE21aRPtc7P8jgGlKTAEntHTprU1P4E2zZp1fr776etMzAIA3+cwUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAECg52QXnHNO15nYQZs4v87hrDuDc+4czrpzOOvO4aynnpOdWVer1WqdoS0AAADThrf5AQAABMQUAABAQEwBAAAExBQAAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExNQ0dejQoVq0aFG98sorTU+hje6///4aHByswcHBWrt2bdNzaKN77723Fi5cWIODg/Xggw82PYc2W7NmTa1atarpGbTRV7/61RocHKzFixfX4sWLa8eOHU1Pok2GhobqC1/4Qn3mM5+pH/7wh03PYZL1ND2Aybdjx4664447avfu3U1PoY1eeOGF2rZtW23atKm6urpqxYoVtXnz5hoYGGh6GpPsd7/7Xb344ov11FNP1dGjR2vhwoU1d+7c+tCHPtT0NNpgZGSkNm3aVDfeeGPTU2iTVqtVu3fvrt/+9rfV0+Ol2HS2b9++Wr16dT3++ON10UUX1W233VZbt26tuXPnNj2NSeLO1DT02GOP1erVq+t973tf01Noo1mzZtWqVavq3HPPrd7e3rryyivr73//e9OzaIOPf/zj9fDDD1dPT0+99tprNTExUTNmzGh6Fm2wf//+uueee2rlypVNT6GN/va3v1VV1fLly+tzn/tcPfLIIw0vol02b95cCxcurA984APV29tb99xzT1177bVNz2IS+e2QaehHP/pR0xM4A6666qq3/nn37t31m9/8ph599NEGF9FOvb29tW7dutqwYUN9+tOfrve///1NT6IN7rrrrvrWt75Vo6OjTU+hjQ4ePFizZ8+uO++8s8bHx+vWW2+tD37wg9Xf39/0NCbZnj17qre3t1auXFmjo6N144031je/+c2mZzGJ3JmCKe7ll1+u5cuX13e+85264oormp5DG91+++01MjJSo6Oj9dhjjzU9h0n2+OOP1yWXXFKzZ89uegptdt1119XatWvr/PPPrwsvvLC+9KUv1datW5ueRRtMTEzUyMhI3X333fWrX/2qdu7cWZs2bWp6FpNITMEU9oc//KGWLVtW3/72t+vzn/9803Nok7/+9a/15z//uaqq3vve99aCBQtq165dDa9isj377LM1PDxcixcvrnXr1tXQ0FDdfffdTc+iDbZv314jIyNvPW61Wj47NU1dfPHFNXv27LrwwgvrvPPOq5tvvrl27tzZ9CwmkZiCKWp0dLS+/vWv109/+tMaHBxseg5t9Morr9Qdd9xRR44cqSNHjtSWLVvqox/9aNOzmGQPPvhgPfPMM/Xkk0/W7bffXvPnz6/vfe97Tc+iDV5//fVau3ZtjY2N1aFDh2rTpk3+8KBpat68ebVt27Y6ePBgTUxM1PPPP19XX31107OYRH4bBKao9evX19jYWP3kJz95698tWbKkvvzlLze4inaYO3du7dy5s2655Zbq7u6uBQsWCGiYwubNm1c7duyoW265pY4dO1ZLly6t6667rulZtMG1115bK1asqKVLl9b4+Hj19/fXF7/4xaZnMYm6Wq1Wq+kRAAAAU423+QEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAZ4177723nnjiidN6zvr162vVqlXtGQQAJ+DvmQLgrPGNb3yj6QkAcMrcmQLgjFm8eHGNjIxUVdUzzzxT11xzTR0+fLiqqr7//e/XnDlzav369VVVdc0119R9991XS5Ysqfnz59fGjRurqmp8fLxWr15dAwMDtWTJkvrjH//YzBcDQMcTUwCcMQMDA/Xcc89VVdXzzz9ffX19tX379mq1WrV169b6yEc+8ta1R44cqQsuuKB++ctf1rp16+rHP/5xjY2N1caNG2v37t3161//ujZs2FCjo6NNfTkAdDgxBcAZczymWq1Wbd++vZYtW1bDw8P1pz/9qS677LKaNWvW266/6aabqqrq6quvriNHjtQbb7xRIyMjtWjRojr33HNrxowZ9dnPfraJLwUAxBQAZ86HP/zhGh8fry1bttQVV1xR8+bNq+Hh4RoaGqpPfepT/3L9e97znqqq6urqqqqqVqv1L9d0d3e3dzQAvAsxBcAZdfPNN9fPfvaz6u/vryuvvLIOHTpUTz/9dC1YsOCUnn/DDTfUE088UWNjYzU2NlbPPvtsmxcDwDvzp/kBcEYNDAzU+vXra86cOVVVNWfOnNq1a1ddcsklp/T8JUuW1N69e2vRokU1c+bMuvzyy9s5FwDeVVfrnd4zAQAAwAl5mx8AAEBATAEAAATEFAAAQEBMAQAABMQUAABAQEwBAAAExBQAAEBATAEAAAT+D14c37BveqQ3AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x=newdf['wind'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcdfa114",
   "metadata": {},
   "source": [
    "## Spliting data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f5cc49ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = newdf.iloc[:,:-1]\n",
    "y = newdf.iloc[:,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "534f9751",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "xtrain,xtest, ytrain, ytest = train_test_split(X,y, test_size = 0.25, random_state = 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "07f519eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#from sklearn.preprocessing import StandardScaler \n",
    "#sc = StandardScaler()\n",
    "#x_train = sc.fit_transform(xtrain)\n",
    "#x_test = sc.fit_transform(xtest)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de432fee",
   "metadata": {},
   "source": [
    "## Random Forest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "e6fdd861",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "28b9546a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(min_samples_leaf=50, n_estimators=50)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = RandomForestClassifier(n_estimators= 50,min_samples_leaf=50)\n",
    "model.fit(xtrain, ytrain)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "9460460b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8261682242990654"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(xtrain, ytrain)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "dc3a54d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.896358543417367"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(xtest, ytest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9ca3fa02",
   "metadata": {},
   "outputs": [],
   "source": [
    "ypred = model.predict(xtest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "5878c6b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['sun'], dtype=object)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test = [0,0,0,46]\n",
    "y_hat = model.predict(np.reshape(test,(1, -1)))\n",
    "ladel_encoding.inverse_transform(y_hat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "b4c5d846",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "68b3014a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9467621366623018"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mse = mean_squared_error(ypred, ytest)\n",
    "MSE = np.sqrt(mse)\n",
    "MSE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "57e6982a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  0   0   0   0   7]\n",
      " [  0   0   0   0  20]\n",
      " [  0   0 165   0   6]\n",
      " [  0   0   4   0   0]\n",
      " [  0   0   0   0 155]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.00      0.00      0.00         7\n",
      "           1       0.00      0.00      0.00        20\n",
      "           2       0.98      0.96      0.97       171\n",
      "           3       0.00      0.00      0.00         4\n",
      "           4       0.82      1.00      0.90       155\n",
      "\n",
      "    accuracy                           0.90       357\n",
      "   macro avg       0.36      0.39      0.37       357\n",
      "weighted avg       0.83      0.90      0.86       357\n",
      "\n",
      "0.896358543417367\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/sonamchoki/opt/anaconda3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1248: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n",
      "/Users/sonamchoki/opt/anaconda3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1248: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n",
      "/Users/sonamchoki/opt/anaconda3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1248: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import classification_report,  accuracy_score\n",
    "print( confusion_matrix(ytest, ypred))\n",
    "print(classification_report(ytest, ypred))\n",
    "print(accuracy_score(ytest, ypred))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
