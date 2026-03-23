{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bb1db8ae-1bc6-4920-a30d-541722c0e824",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q -U watermark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0cc0682a-0d68-4d35-897d-f12dbf681805",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import random\n",
    "from datetime import datetime, timedelta\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f9bd96c7-7965-4872-b023-c7a99eef0295",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Author: Samarao\n",
      "\n"
     ]
    }
   ],
   "source": [
    "%reload_ext watermark\n",
    "%watermark -a \"Samarao\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e6e7a62e-07d5-459d-9d68-d7eabb47fd3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "matplotlib: 3.10.0\n",
      "numpy     : 2.3.2\n",
      "pandas    : 2.3.1\n",
      "seaborn   : 0.13.2\n",
      "\n"
     ]
    }
   ],
   "source": [
    "%watermark --iversions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dfcc7862-a892-48d6-81dd-4cdeaa7048e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def samara_dados_vendas(num_registros = 700):\n",
    "\n",
    "    \"\"\"\n",
    "    Gera um Dataframe do Pandas com dados de vendas ficticios.\n",
    "    \"\"\"\n",
    "    \n",
    "    print(f\"\\nIniciando a geração de {num_registros} registros de vendas...\")\n",
    "    \n",
    "    produtos = {\n",
    "    'Hollow Knight': {'categoria': 'Indie','preco': 7500.00},\n",
    "    'The Last of Us': {'categoria': 'Apocaliptico', 'preco': 250.00},\n",
    "    'Minecraft': {'categoria': 'Indie','preco': 550.00},\n",
    "    'Overcooked': {'categoria': 'Indie', 'preco': 2800.00},\n",
    "    'Resident Evil': {'categoria': 'Apocaliptico', 'preco': 1200.00},\n",
    "    'Enigma do Medo': {'categoria': 'Indie', 'preco': 800.00},\n",
    "    'God of War': {'categoria': 'Ação', 'preco': 4500.00},\n",
    "    'Silent Hill': {'categoria': 'Apocaliptico', 'preco': 600.00}\n",
    "    }\n",
    "\n",
    "    lista_produtos = list(produtos.keys())\n",
    "    cidades_estados = {\n",
    "        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',\n",
    "        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'\n",
    "    }\n",
    "    lista_cidades = list(cidades_estados.keys())\n",
    "    dados_vendas = []\n",
    "    data_inicial = datetime (2026, 1, 1)\n",
    "    for i in range (num_registros):\n",
    "        produto_nome = random.choice(lista_produtos)\n",
    "        cidade = random.choice(lista_cidades)\n",
    "        quantidade = np.random.randint(1, 8)\n",
    "        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))\n",
    "        if produto_nome in ['Minecraft', 'Overcooked']: \n",
    "            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)\n",
    "        else:\n",
    "            preco_unitario = produtos[produto_nome]['preco']\n",
    "        dados_vendas.append({\n",
    "            'ID_Pedido': 1000 + i,\n",
    "            'Data_Pedido': data_pedido,\n",
    "            'Nome_Produto': produto_nome,\n",
    "            'Categoria': produtos[produto_nome]['categoria'],\n",
    "            'Preco_Unitario': round(preco_unitario, 2),\n",
    "            'Quantidade': quantidade,\n",
    "            'ID_Cliente': np.random.randint(100, 150),\n",
    "            'Cidade': cidade,\n",
    "            'Estado': cidades_estados[cidade]\n",
    "        })\n",
    "\n",
    "    print(\"Geração de dados concluída.\\n\")\n",
    "    return pd.DataFrame(dados_vendas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3a2fba57-faf0-4eb6-b75f-682928866203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Iniciando a geração de 700 registros de vendas...\n",
      "Geração de dados concluída.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_vendas = samara_dados_vendas(700)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fae5e550-1158-4d74-83c6-2bb1c3ee5cbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df_vendas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6591bac5-3c3f-4099-a636-120853f2fc11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(700, 9)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1d178426-344d-4ef1-a440-6d8c6e8d14d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.head of      ID_Pedido         Data_Pedido    Nome_Produto     Categoria  \\\n",
       "0         1000 2026-01-01 03:00:00   Hollow Knight         Indie   \n",
       "1         1001 2026-01-01 06:00:00      God of War          Ação   \n",
       "2         1002 2026-01-01 08:00:00       Minecraft         Indie   \n",
       "3         1003 2026-01-01 09:00:00   Resident Evil  Apocaliptico   \n",
       "4         1004 2026-01-01 16:00:00      Overcooked         Indie   \n",
       "..         ...                 ...             ...           ...   \n",
       "695       1695 2026-05-20 12:00:00  Enigma do Medo         Indie   \n",
       "696       1696 2026-05-20 21:00:00  The Last of Us  Apocaliptico   \n",
       "697       1697 2026-05-20 19:00:00   Hollow Knight         Indie   \n",
       "698       1698 2026-05-20 09:00:00  Enigma do Medo         Indie   \n",
       "699       1699 2026-05-20 23:00:00      Overcooked         Indie   \n",
       "\n",
       "     Preco_Unitario  Quantidade  ID_Cliente          Cidade Estado  \n",
       "0           7500.00           4         109  Rio de Janeiro     RJ  \n",
       "1           4500.00           5         148        Salvador     BA  \n",
       "2            549.61           2         141        Curitiba     PR  \n",
       "3           1200.00           4         121  Rio de Janeiro     RJ  \n",
       "4           2546.30           1         110        Curitiba     PR  \n",
       "..              ...         ...         ...             ...    ...  \n",
       "695          800.00           6         120       Fortaleza     CE  \n",
       "696          250.00           1         149       São Paulo     SP  \n",
       "697         7500.00           2         147    Porto Alegre     RS  \n",
       "698          800.00           4         137        Curitiba     PR  \n",
       "699         2790.71           1         136  Rio de Janeiro     RJ  \n",
       "\n",
       "[700 rows x 9 columns]>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.head"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2fd40fb2-191b-45ef-9ec6-9e0fbd40cecd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.tail of      ID_Pedido         Data_Pedido    Nome_Produto     Categoria  \\\n",
       "0         1000 2026-01-01 03:00:00   Hollow Knight         Indie   \n",
       "1         1001 2026-01-01 06:00:00      God of War          Ação   \n",
       "2         1002 2026-01-01 08:00:00       Minecraft         Indie   \n",
       "3         1003 2026-01-01 09:00:00   Resident Evil  Apocaliptico   \n",
       "4         1004 2026-01-01 16:00:00      Overcooked         Indie   \n",
       "..         ...                 ...             ...           ...   \n",
       "695       1695 2026-05-20 12:00:00  Enigma do Medo         Indie   \n",
       "696       1696 2026-05-20 21:00:00  The Last of Us  Apocaliptico   \n",
       "697       1697 2026-05-20 19:00:00   Hollow Knight         Indie   \n",
       "698       1698 2026-05-20 09:00:00  Enigma do Medo         Indie   \n",
       "699       1699 2026-05-20 23:00:00      Overcooked         Indie   \n",
       "\n",
       "     Preco_Unitario  Quantidade  ID_Cliente          Cidade Estado  \n",
       "0           7500.00           4         109  Rio de Janeiro     RJ  \n",
       "1           4500.00           5         148        Salvador     BA  \n",
       "2            549.61           2         141        Curitiba     PR  \n",
       "3           1200.00           4         121  Rio de Janeiro     RJ  \n",
       "4           2546.30           1         110        Curitiba     PR  \n",
       "..              ...         ...         ...             ...    ...  \n",
       "695          800.00           6         120       Fortaleza     CE  \n",
       "696          250.00           1         149       São Paulo     SP  \n",
       "697         7500.00           2         147    Porto Alegre     RS  \n",
       "698          800.00           4         137        Curitiba     PR  \n",
       "699         2790.71           1         136  Rio de Janeiro     RJ  \n",
       "\n",
       "[700 rows x 9 columns]>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.tail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2832ece5-2311-4e8e-9a12-ea2524f85325",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 700 entries, 0 to 699\n",
      "Data columns (total 9 columns):\n",
      " #   Column          Non-Null Count  Dtype         \n",
      "---  ------          --------------  -----         \n",
      " 0   ID_Pedido       700 non-null    int64         \n",
      " 1   Data_Pedido     700 non-null    datetime64[ns]\n",
      " 2   Nome_Produto    700 non-null    object        \n",
      " 3   Categoria       700 non-null    object        \n",
      " 4   Preco_Unitario  700 non-null    float64       \n",
      " 5   Quantidade      700 non-null    int64         \n",
      " 6   ID_Cliente      700 non-null    int64         \n",
      " 7   Cidade          700 non-null    object        \n",
      " 8   Estado          700 non-null    object        \n",
      "dtypes: datetime64[ns](1), float64(1), int64(3), object(4)\n",
      "memory usage: 49.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df_vendas.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8f5eb547-a6d2-414a-8757-0030a7897db8",
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
       "      <th>ID_Pedido</th>\n",
       "      <th>Data_Pedido</th>\n",
       "      <th>Preco_Unitario</th>\n",
       "      <th>Quantidade</th>\n",
       "      <th>ID_Cliente</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>700.00000</td>\n",
       "      <td>700</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>700.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1349.50000</td>\n",
       "      <td>2026-03-11 23:31:06.857143040</td>\n",
       "      <td>2198.756529</td>\n",
       "      <td>3.978571</td>\n",
       "      <td>124.727143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1000.00000</td>\n",
       "      <td>2026-01-01 03:00:00</td>\n",
       "      <td>250.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1174.75000</td>\n",
       "      <td>2026-02-04 23:15:00</td>\n",
       "      <td>543.795000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>113.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1349.50000</td>\n",
       "      <td>2026-03-11 23:00:00</td>\n",
       "      <td>800.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>124.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1524.25000</td>\n",
       "      <td>2026-04-15 18:30:00</td>\n",
       "      <td>2791.362500</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>138.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1699.00000</td>\n",
       "      <td>2026-05-20 23:00:00</td>\n",
       "      <td>7500.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>149.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>202.21688</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2371.654626</td>\n",
       "      <td>2.064995</td>\n",
       "      <td>14.707199</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        ID_Pedido                    Data_Pedido  Preco_Unitario  Quantidade  \\\n",
       "count   700.00000                            700      700.000000  700.000000   \n",
       "mean   1349.50000  2026-03-11 23:31:06.857143040     2198.756529    3.978571   \n",
       "min    1000.00000            2026-01-01 03:00:00      250.000000    1.000000   \n",
       "25%    1174.75000            2026-02-04 23:15:00      543.795000    2.000000   \n",
       "50%    1349.50000            2026-03-11 23:00:00      800.000000    4.000000   \n",
       "75%    1524.25000            2026-04-15 18:30:00     2791.362500    6.000000   \n",
       "max    1699.00000            2026-05-20 23:00:00     7500.000000    7.000000   \n",
       "std     202.21688                            NaN     2371.654626    2.064995   \n",
       "\n",
       "       ID_Cliente  \n",
       "count  700.000000  \n",
       "mean   124.727143  \n",
       "min    100.000000  \n",
       "25%    113.000000  \n",
       "50%    124.000000  \n",
       "75%    138.000000  \n",
       "max    149.000000  \n",
       "std     14.707199  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "22cda687-9cd1-4e7d-b31d-0f0cf2fe8102",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ID_Pedido                  int64\n",
       "Data_Pedido       datetime64[ns]\n",
       "Nome_Produto              object\n",
       "Categoria                 object\n",
       "Preco_Unitario           float64\n",
       "Quantidade                 int64\n",
       "ID_Cliente                 int64\n",
       "Cidade                    object\n",
       "Estado                    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e508b166-2fbf-4ac2-85aa-0d8b2b4d27c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d4bc3c99-9475-4b90-aa27-94f1ff025775",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e83e95b3-9773-41c6-9419-dd5c3a0e409d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d6f8edfc-0434-42d1-8211-b23146fc21c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 700 entries, 0 to 699\n",
      "Data columns (total 11 columns):\n",
      " #   Column          Non-Null Count  Dtype         \n",
      "---  ------          --------------  -----         \n",
      " 0   ID_Pedido       700 non-null    int64         \n",
      " 1   Data_Pedido     700 non-null    datetime64[ns]\n",
      " 2   Nome_Produto    700 non-null    object        \n",
      " 3   Categoria       700 non-null    object        \n",
      " 4   Preco_Unitario  700 non-null    float64       \n",
      " 5   Quantidade      700 non-null    int64         \n",
      " 6   ID_Cliente      700 non-null    int64         \n",
      " 7   Cidade          700 non-null    object        \n",
      " 8   Estado          700 non-null    object        \n",
      " 9   Faturamento     700 non-null    float64       \n",
      " 10  Status_Entrega  700 non-null    object        \n",
      "dtypes: datetime64[ns](1), float64(2), int64(3), object(5)\n",
      "memory usage: 60.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df_vendas.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "79ec93d7-1f35-4f3f-847a-69abbb1f0b2e",
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
       "      <th>ID_Pedido</th>\n",
       "      <th>Data_Pedido</th>\n",
       "      <th>Nome_Produto</th>\n",
       "      <th>Categoria</th>\n",
       "      <th>Preco_Unitario</th>\n",
       "      <th>Quantidade</th>\n",
       "      <th>ID_Cliente</th>\n",
       "      <th>Cidade</th>\n",
       "      <th>Estado</th>\n",
       "      <th>Faturamento</th>\n",
       "      <th>Status_Entrega</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>2026-01-01 03:00:00</td>\n",
       "      <td>Hollow Knight</td>\n",
       "      <td>Indie</td>\n",
       "      <td>7500.00</td>\n",
       "      <td>4</td>\n",
       "      <td>109</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>30000.00</td>\n",
       "      <td>Rápida</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>2026-01-01 06:00:00</td>\n",
       "      <td>God of War</td>\n",
       "      <td>Ação</td>\n",
       "      <td>4500.00</td>\n",
       "      <td>5</td>\n",
       "      <td>148</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>BA</td>\n",
       "      <td>22500.00</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>2026-01-01 08:00:00</td>\n",
       "      <td>Minecraft</td>\n",
       "      <td>Indie</td>\n",
       "      <td>549.61</td>\n",
       "      <td>2</td>\n",
       "      <td>141</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>1099.22</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>2026-01-01 09:00:00</td>\n",
       "      <td>Resident Evil</td>\n",
       "      <td>Apocaliptico</td>\n",
       "      <td>1200.00</td>\n",
       "      <td>4</td>\n",
       "      <td>121</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>4800.00</td>\n",
       "      <td>Rápida</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>2026-01-01 16:00:00</td>\n",
       "      <td>Overcooked</td>\n",
       "      <td>Indie</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>1</td>\n",
       "      <td>110</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID_Pedido         Data_Pedido   Nome_Produto     Categoria  Preco_Unitario  \\\n",
       "0       1000 2026-01-01 03:00:00  Hollow Knight         Indie         7500.00   \n",
       "1       1001 2026-01-01 06:00:00     God of War          Ação         4500.00   \n",
       "2       1002 2026-01-01 08:00:00      Minecraft         Indie          549.61   \n",
       "3       1003 2026-01-01 09:00:00  Resident Evil  Apocaliptico         1200.00   \n",
       "4       1004 2026-01-01 16:00:00     Overcooked         Indie         2546.30   \n",
       "\n",
       "   Quantidade  ID_Cliente          Cidade Estado  Faturamento Status_Entrega  \n",
       "0           4         109  Rio de Janeiro     RJ     30000.00         Rápida  \n",
       "1           5         148        Salvador     BA     22500.00         Normal  \n",
       "2           2         141        Curitiba     PR      1099.22         Normal  \n",
       "3           4         121  Rio de Janeiro     RJ      4800.00         Rápida  \n",
       "4           1         110        Curitiba     PR      2546.30         Normal  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "35065c7d-552c-4a6e-9554-530ca730c4a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "top_10_produtos = df_vendas.groupby('Nome_Produto')['Faturamento'].sum().sort_values(ascending = False).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5f0b84b6-6bc5-4e4b-bfb6-a4b4fc4928a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Nome_Produto\n",
       "Hollow Knight     2392500.00\n",
       "God of War        1593000.00\n",
       "Overcooked         837717.94\n",
       "Resident Evil      432000.00\n",
       "Enigma do Medo     287200.00\n",
       "Silent Hill        203400.00\n",
       "Minecraft          187460.72\n",
       "The Last of Us      95000.00\n",
       "Name: Faturamento, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_10_produtos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7a492571-559f-41b8-8ee5-cd8c7adf6f05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAKyCAYAAADIG729AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAaUlJREFUeJzt3Qd0VVUaN+4dggg62Bh7HSuiWFBQx94b9t5772MXG/be62dBsYzj2Av23rCNBRuOY8OuYEGlKOS/3v39b74kBEhIDrkkz7PWXeG2c/c9d+eS33n33qeiqqqqKgEAAADNrl3zbxIAAAAIQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AYDCVFVVtXQTAKBFCd0ANMmll16aFllkkUZdvvjii1Qu7rnnntymF198cbyP+eGHH9Ipp5yS1l577bTEEkukNddcM5177rnpt99+a/Dr3HXXXePdH4svvnj6+9//nnbdddd05513prFjx6aWcswxx+Q2/fvf/27Sdj755JO01157pc8//zy1tOhvNff3Bx98MMHHjx49Oi277LLVj//zzz8n+bVLn/sRRxyRmsuAAQPyNqPPNKRtjz/+eH78hhtumMrl++LCCy+c5H1U+jxXWWWVAlsK0HzaN+O2AGiD4o/fjTbaqNZtQ4cOzSF2mmmmyQG1rri9HLz99tvp1FNPneBjvvvuu7TtttumL7/8Mi288MJptdVWS4MGDUrXXntteu6559Ktt96a/vKXvzT4Nbt06ZLDUk0RnGKfvfLKK+mll15KL7zwQrrgggvSlGzPPfcsq4MrNT388MOpa9eu473/2WefTcOHD0/laq211kozzDBD9e/ZxMJnHFgKW2655WRqIQA1Cd0ANMk666yTLzW9/PLLOQzMOOOM6bzzzkvl6Mknn0xHH310+vXXXyf4uNNOOy0H7r333jsdfvjh1ZXQo446Kj300EPpsssuy9XhhlpggQXGu0/efffdtNNOO6UHH3wwbbDBBjlcTanKcVh5HOwZNWpUDt2HHnroBCvJU001Vfrjjz+a/JoxOmLJJZdMnTt3Ts2lQ4cO+UDXTTfdlO6///4Jhu6ffvopPf300/n9bLLJJqkcFbGPAMqJ4eUAtCnffvttOvbYY9P++++fQ9Vf//rX8T42hkY/9thjafbZZ08HH3xwrdATFfJpp502/etf/0ojR45slrYttthiaeutt87/fvTRR5tlm/w/EeqWW265PPR98ODB9T5mxIgR6amnnkorr7xys71mHGiZZZZZUnMqVa1j6Hi0eXziAE708xhxMtNMM6VyVNQ+AigXQjcALSKqb3vssUfq1atX6t69e1p33XXzPOmozNU3hL13795p2LBhuaocwalHjx552HdULRsj5pLGHNIIuBGY559//gkOM4751auuumquFNYNCssvv3z6/fffc2W/ucw999z5ZwwdLonqd+yDDz/8MO288855f6200krpkUceqX7Mf/7zn3TAAQfkNsUc8dVXXz2ddNJJ6euvv673dT799NNcrY/tLLXUUmmHHXYY7/uY0DzveE7cF22seT1GB4QYBVF3Hn98jmeffXb+zKOt0QeiLzzzzDMT7CsRhEvvLQ6c/O9//0uNtf766+ef4+s3EbjjM43+Nj4R2k888cTc/th3Mc8/RiWcfPLJ+aBOTeObr/zGG2/kAz9rrLFGfk/xOcSBnZjy0BAxPD76cLT1iSeeGO/j7r777vxzq622qnV7TGGIKQDxuxT9KfZLzLeO7dU3fzraWjpgteKKK+bnxBzxfv36pTFjxtQ7LSPWQYjPKvbP5ptvXqu/NmQfxWiJ+B3dbLPN8n6Oz/+cc86Z4EGu6Hfx2ZT2a/w+xO/Fm2++Od6h9zvuuGOe8hHtjKp7tPubb74Z72sANJbQDcBkF8Or99lnnzx/Of7Yjj/Mo1oX86Tjj/MhQ4aM85y4PwLnAw88kP/gjz/CY271IYccki655JIGv3aE7Ah8ESDjtSckQm6Iudz1WXDBBWs9rjn897//zT+jul7XQQcdlINmHARo3759Dl3hlltuyaE5qp7zzDNPDhxxkOC2225Lm2666ThB7p133skV9XvvvTdPAYjhyRHOd9999xwGmyJGDsTQ59K8/aiw1rweowdimPP111+fP9Noa3wO0RdiCP9FF11Ua3vxnvbbb78c5qMaGo/v2LFjDmoRJD/66KNGtS9CVey78YXuGFreqVOn3Cfr89prr+UQGGEw5vLHvlt66aXzYnv//Oc/84GgiU1ZiAAYi+ZFwI/POd7TzDPPnEPp9ttvnwYOHNioavd9991X7/3RV+J3ZM4556y1jsCVV16ZP+vY53/729/yOgXR5pgqEa//888/j7Ot77//Pu/vGPnRrVu3/J4//vjjdNZZZ6UzzjhjnKAe/Sv6ZfTD2H4E5Tio0JiDZDH9IwJ0HCCK8By/bzfeeGP+na/PW2+9lTbeeOP82cRnHPt13nnnzX1ou+22y7fX1L9///waMa0j3lP8XsUBhGh37NuaB74AmqQKAJrZwIEDqxZeeOGq1VdffZz7nnjiiXxfr169qt5+++3q20eNGlXVp0+ffN9mm21WNXbs2Or74ra4rLDCClWDBw+uvv2tt96q6tGjR9UiiyyS/z0pdtxxx7ztF154YZz79t1333zfI488Uu9z+/fvn+8/44wzJvo6d955Z35svN74vPjii1WLLbZYftxLL700ThtXXXXVqmHDhuXbxowZk3++9957VV27dq3q3r171dNPP139nLj/0ksvzc9bZZVVqkaMGFF9+8Ybb5xvv+KKK6ofP3r06Kpjjjmmel/ffvvt1fcdffTR49xW97Ou+77is4/bP/300+rb4jONzzZuP/744/NnXhKfX/SJuC/6SMmaa65Z1a1bt6r//ve/tbZz2mmn5cced9xxE9nzVVVDhgzJj1155ZXz9d133z1fr9mXwvDhw/N+POyww/L10r74448/qh/Tu3fvevvEd999V/2e77333nE+98MPP7z6tp133jnf9txzz9XaRr9+/fLtu+yyS1VD/PLLL1VLLLFE3j9Dhw4d5/7zzjsvby/6Qc0+VtoX0XdK4rMoff4121rad3HZfvvta71O6Xc5Xv/nn3+uvn2fffbJt59wwglVf/75Z/VndtFFF1Vv64ILLpjgPnr44YfzbfH5f/XVV9W3Dxo0qGrZZZet9XmGkSNH5uul91vz+yN+L+JzjXa+++671e93ySWXzH3u22+/rX5sfNYHHnhg3s7ll1/eoM8BYGJUugGYrG644Yb8M4Y2R8W65jzpGJ4blamoPNVX7YuhrTWrzjEcNKqgMQw1qozNrTTUNiqr9SndXndI7oRE9TGG0da8RAUwqsFR/Yz5t7vsskuu7NUVFeKoTId27dpVV+tiCHwMFY5KXUncf+CBB+ah2zFUNhbcKg1Dj1NmLbroonnflURFMvb/hOa4N1VUieOzjWp8DH2Pz7zmZxlVxxAjHmpWWKNqGau+l1RUVKR99903nXDCCbnq3FxDzKMiGgutxSJ29YlTxMWQ5S222GKcxQOjUl1a+G5iq7bHe6pvNENUmaOPRxW6IWKKQ1TuY/X7WNSvpugTUQGPfhCjR0quu+66/PO4447LfaAkPouoKsd+jmp/3WHyIfZ3zXnhUUmea6658utH1TtEX4sKfmzn+OOPT5WVldWfWfTzmq85IaXf55jaUHM/xf6P4eJ1xfuPNvfs2TP3+3i9kvi9iNPXRTtjOHyI1eljpEWMaoiV4Euir8WCifG7UPP3CaAphG4AJpv4ozdCX/xBHPNh64o/eEthpu784giF9T0nQkd9j28ONQPDhFbobsxK3TFkNQJwzUvMWY7hvRHaLr/88hyI6lPfcPhXX321VpCsqxQg43RkNR9f34rXU089daHnPi61Id5nfNZ1rbfeenmfxzDhWCE+RIiKockRrmP4cwyVj0AZoS7m4sb5tBsr+kz0p7qhO8LmdNNNN959EAvnnXnmmeMMp475yzEfvXT+71LbxyfeUylkx1SL2C9xsCWCbxx4acxnUBpiXjqoUhIHrSIAx/zrOeaYI98WQ6fjwEdYYYUVxtlWBNBoW83H1byvvv5XWvystJhb6TOO7dc8qFL6PWrIivzx+cbrR1+Iue511T3gUfN1G/p7EP0npprEtIqYgnHNNddUL64333zz5eHopekbAE3llGEATDaxSFqEi6jWju/c1lE5q1kNLIlqV90/4ku3l4JPcyvNQ47qZ31Kt0cgaaioPMepniZFBMK6Su875u02ZH+WHj/rrLNO8PFFKL32+F4j9ndUUqOtsdjabLPNlk/ZFpXLmJscC33FJSqTUYWMwBn7s7Gmn376PMc5gnLMoV9ooYVy34zT3MWIg/r6WU1x4CjWBHjvvffyHPXSSIfSwZmJHYQ58sgj84JfcZ73CHtxifceC4XFnOTGnCouFkKLkQMxFz/WQigtxFdaQK3mubnjPZbC8cT2W90F+KKqXt/Bp9LBk9J7bo7+VfqeiL5Q3yiTOIhQOiDW0N+D0n6JufclsX5AVN9j9Ekc/IhLHESI+fwxNz/meQM0B6EbgMmm9If5+CrHNR9TN/iUhlOP7/H1VU6bqlTFq3sAoKR0ewwtnhzq2wcT26d19+eE9v2k7MeoSjZUQ0YE1G1vBO877rgjvf7663n4dwTjqEjGInBxiWHDdVe9boioiEbojmHJEbpjgbAIerEi94T07ds33XrrrTn0xQriUZ2PBb7iPNMRoq+66qqJvnYccIoh9O+//34+NVysJB6L28VCanGJqmysst8Q8XnG8PEIkDGcPIZexzD4eD8RWmMhu5LSKuOxb+sbNVJTTPOo+zoNbc+ENNfvad3fhYb+HtQ8C0FU7mN0Qywo9+STT+bPIRZtiwXXbr/99jycPhYoBGgqoRuAySYqlPFHb1SyYjh1fdXu0srlNefwlgJu/OFc94/q0qmpIpw1t9L88fGdmqq00vjEVkEvUhwYiDnEcYnwOLH9WdpPpf1WV30jBkr7vL5TQ9V3ircJtXVCc54jLEaFOwJtzXm2YZlllsmX0hD9O++8MwfTmKMcpysbX2V1fKKaXBpiHtXOCF+xj+obdl0SQ5MjcMfoinjdWE29psaevi7mN8clVuOOOcZxAOD000/PbYl5/bFCf0NE6I4V/GNl/wjdEeSjoh1DpGuGzNLvX0zziCHyE6voT4pJ6V91xUiYmOoQfSv6RAzrr+nHH3/MB0ga07fG971SGsJeGsb+1Vdf5XUSYu53VL5jFfa6pwsEaCxzugGYbOKP1zjVUFRHoxJXV4SB0u0xbLam+OO7NB+5pqh+hhia29xK24yFoeoGzghJMY88hgWXwmBLKM0PHt85kEsLbJX2ZylURmWv7nuK61GtrasUeuo7hVJjTjFWamucVzo+67oitEbfiHnaUcmMxbliuHcsEldTBKc4vVgc7IjH17fo18TEcOkIWnFAJcJ0fJZR/a07bLmm0rmeY05x3cAd+660+N+EKvq//PJLDsnxvuq2JwJeKfyN7/zq9YkDDvG82F9xCrUI7XWHlocI2RHkY5/V9zlHu2NOeQytbuj5wuuKBQDjs4sRCfE7W1esXzAxcZAn+mm0s75zkNd3PvdS35rQqeBqDquPzzxGO8TicXWHrsfibTGVI6YNxO85QFMJ3QBMVlHBC+ecc06eE1sSlasYuhtzZKP6V1+QjftrDvWOwBfDeSNMxKJUzS3mh8b8zqienXvuudVhKhbKij/WI1REQBnf/PTJIRYTi6AY84Kff/756tujrbHwWByoiFBWmiccK8ZHqP3kk0/yZ1AaHh4/o7L32WefjfMapUr+Pffck0NjSQSXuuc+LolKZagZWiLwxDzZeI1TTz21VrUyhldHe0rvqTTEOebgxvuqG6bi8RGY44BALIg1KUqLbsVK6hGaJza0vLRyfAxHLs2NDvHvGIpcGvkwvjUAQoS52NdxbvfSSv4l0c9ivniE1liluzFKATvOXx7ti4NbdQ8MhAjVIfZ/zd+/aFMMUY/nRlU4hs5Pijgg0rt379xP+vTpU2tRuaggN3TBw1I7o0/UHGkSBxain9b3WUa1O/pknIe85oGPZ599Ng/nj9+TqP6HGBUS3zXRp2PqQt0DA9H+mH9ec7V2gElleDkAk1WEvzgl0vXXX5+DQoTrCDOxYnWsthxBN4YN1zd/OYakRzUyqmlRhYo/sOOP6wjjf/vb3wppb4SpOM1VDDeNClv8sR6LesUw1FjdOBb5akkRzuI0UzEseY899siVzBjiGytpx/zUGFJ88cUX1zowECtwx5DsCH0RMCJgxTzpeHw8v1TRLYk5xldccUUOKVHljdAeYTgOesSq4qVFu2qKwBwBKYZOx36KxcNiMasLLrggH3i57bbb8mvHXOgYRhyrVUfwjQp2aXXqCEmnnHJKOuigg6q3E0EohhdHUIrHx+czqQc9Yr5zHByIdsaQ8YmNWIhgFwcyIjBHP459FaEy9kMcXIi+EcG75mJd9Yn+GgcW4nOIucMRjqNvx3uKwB6nQyst/NVQcfquCIgRbONgxlZbbTXR3794TOzTCKvRXyJsx6KAMVS9KUPPoz/G9mKUReyb+Ixj2xHy42BAQ0ZHRKV7n332SVdffXVeXTx+56MCHgcFor/WHXUR7Y5+Hv0nDh5EmI7HxSiIeL3oS3EQIE5NF+I7J/pkfAYxbzs+y9gP8fjo/zH3vG4VHGBSqXQDMNnF+ZgjxMWQ5/jjPMJXVCzjvNER4MYXoG+55Za8anWE7fgDPk6HFCuBx7DcosRBgFjIKwJKBKsYah6BJIJRBJy6801bQgTom2++OQevCM4xdDwqlxFuY3GtCDo1xWrXsfp2jA6I03HFe4ph8hEo6zs3cbzHCMkxLDrCSxx8iCp/nMs4zsVcnzjtWVS2I4DGUOPSeZzjs43PeLfddsv7MdoaQ6JjKH8EwThHct3Te8X86TiNVhzoiOHG8fi4Hvu/KZ99hPXSFIII1BNbBCweHyE5DhZFWI8KarQlRg/EgaJoT2wjKvN15xzXFCE05obHAaSoqMY+iAM7Efoj8B522GGTNHUjzuMerxuf1/hOnVX6/YtqcATZ6C/xecZBrnhfsThdU6dLRPiP9xcBONoV/SsOJsRK9KVKc0P84x//yAE6DgzEQZkY8h7vMarW9X1WPXr0yH0r+kS8XvSVmFseB42i/9ZdFC2q6fG5xdD0qKaXHh8jHuJ33nm6geZSUdWYk4sCQAsoDW+OYFLEKuUAAEVR6QYAAICCCN0AAABQEKEbAAAACmJONwAAABREpRsAAAAKInQDAABAQZx3hUkS53/9888/83k9J3ZeUwAAgClVzMiO/BOnLY3801hCN5MkAvegQYNauhkAAACTRffu3VOHDh0a/Tyhm0lSOsLTrVu3Sep40NzGjBmTDwTFl2FlZWVLNwcy/ZJyo09SjvRLyr1Plq5PSpU7CN1MktKQ8uiEvhwpJ/ok5Ui/pNzok5Qj/ZJy75OTOq3WQmoAAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGWo1OnTq1dBNgHPol5UafpBzpl7Rm7Vu6AUzZKisrW7oJUN0Xu3Xr1tLNgFr0S8qNPkk50i8JY6uqUruKitQaCd00yYDPhqcfRle1dDMAAIApVJeO7dPG83VOrZXQTZMMGzUmfTtS6AYAAKiPOd0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRusjFjxqQhQ4a0dDMAAABalVYRutdYY4101113jXN73Bb3NUTNx7788stpkUUWafZ2TqxtI0eOTPvuu29ac80108cffzzRbZx44on50hA77bRTuvTSS8d7/2GHHZbuueeeBm0LAACAhmnfwMdRsJ9++ikH7j///DPdfvvtqUuXLhN9zimnnNJsr//jjz8227YAAABoRZXuhho8eHDaa6+9Uq9evdIqq6ySTj755DR8+PBJft7PP/+cFltssfT+++/nx40aNSotscQS6dxzz61+7sEHH5wuvvjiCW7/66+/TjvssEOaYYYZ0k033VQduKMavt1226XTTjstLb/88mmFFVZIffr0SX/88Ue+/5hjjsmXkv79+6fVV189LbfccrlyfdBBB9Wqbn/22Wdp9913Tz179szV9IcffjjfHtt87bXX0tVXX52DPwAAAM2j1YTuvn37pmWXXbbWJW6rWcndeeed04ILLpieffbZdOedd6ZPPvkkHXXUURPc7oSeN/300+cgHreHV155JVVUVKQXX3wxXx89enR6/vnn0zrrrDPe7X/00Udp2223TXPMMUe6/PLLU6dOnWrd/5///CeH8Oeeey6H4gEDBqRHH310nO08+OCD6bLLLkvnn39+fs14/3Uf98ILL6TDDz88D5/ffPPN07HHHpsD/Omnn54fv88++6SrrrqqgXscAACgedeZGlMml7rtaYpWM7z8pJNOykGypqgURxANTzzxRJpqqqnSEUcckSorK1PHjh3TCSeckDbccMP0/fffj3e7E3veWmutlYNwBNYIu9tss026+eab07Bhw9I777yTZpxxxrTooouOd0h5VLiXWmqpHNgjgNedSx6vF9XnCPNRRY/7I/TXdccdd+TX7tGjR74e27377rtrPWaDDTbIlfnSvy+55JI0dOjQNNtsszV4PwMAABRh8ODBacSIEalcDBo0qFm202pC98REuIxqcgTnkrnmmiv//PLLLyf5eRG6zzzzzDzcPKrRZ5xxRg7QAwcOzBXlCVW5oxIeVeb1118/HXrooWn//ffP4TmCeklUuSNwl8QBgKqqqnqHqK+77rq1bpt77rlrXY/h6zW3E2IOOQAAQEtbpODFrBsqKtsRuLt3755zYOl6auvDyydmzjnnTF999VWtoQGff/55/jnzzDNP8vNmnXXW1LVr11xV/+GHH/IHs9JKK+Uh5k8//fQEQ/css8ySA3eI8N2hQ4c8F3tSgnCpnTXVvQ4AAFCuKisry+ZStz1N0WZC96qrrpp/nnfeefnUXDE0PIJuLFAWgbUpz1t77bXTlVdemW+LD2TFFVdMDzzwQBo7dmweOt4Q0047bR4K/9Zbb6Wzzz670e9v6623zquev/322zm0x9zzN998s8HPj8DfkEXlAAAAaLg2E7o7d+6c+vXrlz788MMcpHv37p1D88RWFm/I82KIeSy4FmE7LLPMMnlIeNxec2j4xCywwAJ5pfJYhby+845PSAwt32OPPfIQ9b///e/ppZdeSosvvnj1MPKJ2XTTTXNQ33777Rv1ugAAAIxfRVV9E4SZ4nzwwQf5AEHNqn0sLBcro0cVvLnFcPuopL8zzXzp65G6EAAAMGlm7VSZduv6/9a1ammlrBOjlktzumteb6w2U+lu7WLhtljlPIa/x3GUWFE9VkOPc3sDAADQMtrM6uWt3Y477phXU99ss83Sb7/9luaff/48z7zuCuYAAABMPkJ3K9G+ffvUp0+ffAEAAKA8GF4OAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFaV/UhmkbZpq6Mo2tqGrpZgAAAFOoLh1bdyxt3e+Owm0wb+dUWVnZ0s0AAACmYGOrqlK7iorUGhleTpOMGTOmpZsA1X3xvffe0ycpK/ol5UafpBzpl4TWGriD0A20GiNGjGjpJsA49EvKjT5JOdIvac2EbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURuoFWo1OnTi3dBBiHfkm50ScBJq/2k/n1aGUqKytbuglQ3Re7devW0s2AWvRLyk1L98mxVVWpXUVFi70+QEsQummSAZ8NTz+MrmrpZgAAZa5Lx/Zp4/k6t3QzACY7oZsmGTZqTPp2pNANAABQH3O6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIK0+dD91VdfpZNOOimtscYaaamllkq9evVKe+yxR3rhhReatN1FFlkkvfzyy5P03BtuuCH17NkzXz744IPq28eOHZuWX3759O9//7vW4/v06ZNf77nnnqt1+/bbb5/OPvvsSXwHAAAANFWbDt0ffvhh2njjjdPo0aPTNddck15//fX06KOP5tsOOOCA9Mwzz7RIu2699da0//77p1dffTV17dq1+vZ27dqllVdeOQ0cOLBWEH/qqafS0ksvnR577LHq23/77bf09ttvp9VXX32ytx8AAID/q02H7hNPPDGtuOKK6cwzz0wLLLBAqqysTDPMMEPaZJNNcvX7jz/+qH7s448/njbffPPUo0ePtO666+ZqdATeEI+LbSy33HK5En3ttddO8HW//PLLdOihh6YVVlghv/7hhx+evvvuu3xfXP/888/TBRdckHbeeedxnrvaaqvVqqD/5z//yWF8v/32S08++WSqqqrKt0dgn2aaaXJ7v/322/x6Uc1fcskl05prrpnuuOOO6m1Elfy0007L7d93332bYc8CAADQpkP3N998k95444207bbb1nv/ZpttltZaa63876gsR2jdc8890yuvvJIDcb9+/VL//v3z/VdccUV6+umnc5CN4BsV9PGJgL777rvngB9V9YceeijfHmH3zz//zMPa55hjjtS3b9/q7de00korpWHDhqWPPvooX3/iiSdymI4AH9Xtt956K98e21lllVVS+/bt0/HHH5+mmmqq9OCDD+aQvuOOO6ZTTz01P74kgn68h3POOadJ+xUAAID/p31qw6E7zDbbbNW3vfTSS+mggw7K/x4zZkyaZZZZ0iOPPJLuuuuuXB3eYIMN8n2LLbZY2nvvvdNNN92Udt1113Tvvffm0Dz33HPn+yPk3nffffW+7muvvZaGDBmS7rzzzvSXv/wl3xYBO+aSv/POO3le+YRMP/30eSh5HAhYcMEFc+iOOd0dOnTIgTyuxzbivcQQ9RBV7GmnnTYH75jDHv8eOXJk+vnnn/O/Q+/evVOnTp3yBQCgKPE3FtTXJ/QNyrVPNrVvttnQPfPMM+efMfT6b3/7W/53VIsjFIcI2pdddln+99ChQ9Oiiy5a6/lzzTVXHiYeYmj47LPPXn3fdNNNl8NxfWJbM844Y3XgDvHvGNYe25tY6A6rrrpqDt0R1L///vvc7hAHBqICv9NOO6VPP/00z/8OEfKjgh23zTfffGneeefNt5eGx4c4wAAAULTBgwenESNGtHQzKEODBg1q6SZAIX2yzYbuOeecM3Xv3j2vBB7zsCf22Bh+XVME2VJwj2p5XC/5/fff0/Dhw8e7rR9//DH9+uuv1cE7Hhu3lbY3MTGvO8J1DAePYB1V7lIYj6r3gAED0rLLLps6d+6ch7Pvs88+6R//+EdezbyioiJX1OtW4uN2AICixVoyUFNUESPcxN/mMQUTyq1Plq5PqjYbusMZZ5yR5zefcMIJeZ51VIFjnnMsmnbppZemWWedNT9uiy22SDvssEOef73OOuvkI7Sx2vnWW2+d799qq63y4mmxEFlUwM8666zxDkGIDy6GhcdCbSeffHK+LX7OM888edGzhlh44YXzMPDbb789HXjggdW3RwU9KuU33nhjHvYeInTHUPKOHTvmYB3Dy88999zq+wAAJiehign1Df2D1tgn2+xCaqXw+sADD+RAGnOyl1lmmVwtjjAbi6aVFjKLFb8vvvjiHLSjghxBd7vttqte6XuvvfbKpxmLAB/zqqPCHMPF6xMLm1199dV50bRYBT1O6RXhNyrXcV9DxSJpEaCj6l1TDDGP22NxtRArmMfBhcsvvzzPBY8V0WOF9L/+9a8TXPANAACApquoKp1jChohKvlvvvlmemea+dLXI3UhAGDCZu1UmXbrOmNLN4My/rsyRmyqdFOOfbKpfbRNV7oBAACgSEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUJD2RW2YtmGmqSvT2Iqqlm4GAFDmunT0ZyfQNvn2o0k2mLdzqqysbOlmAABTgLFVValdRUVLNwNgsjK8nCYZM2ZMSzcBqvvie++9p09SVvRLyk1L90mBG2iLhG6g1RgxYkRLNwHGoV9SbvRJgMlL6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRtoNTp16tTSTQAAgFra174KjVNZWdnSTYDqvtitW7eWbgZNMLaqKrWrqGjpZgAANCuhmyYZ8Nnw9MPoqpZuBjCF69Kxfdp4vs4t3QwAgGYndNMkw0aNSd+OFLoBAADqY043AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUJA2GbrffffddPDBB6fll18+Lb300mnttddOZ599dvrpp5/SlOSYY47Jl+Zw1113pTXWWKNZtgUAAEAbDd1PPfVU2n777dPf/va3dO+996b//Oc/6aqrrkpDhgxJm266afr2229buokAAAC0Em0qdI8ePTodf/zxaZ999kmHHXZYmnXWWVNFRUVaYIEF0iWXXJJmm222dPrpp+eK77/+9a/q540ZMyatvPLK6aGHHsrXX3zxxbTlllumZZddNm244Ybpvvvuq35sVJ6jir7++uvnSvrnn3+eA/2+++6blllmmbTCCiukk08+ObclDB48OO21116pV69eaZVVVsn3DR8+vHp7jz/+eNp8881Tjx490rrrrptuuOGGNHbs2HHe25dffpnWXHPNdMYZZ6Sqqqq8/YsvvjjfFtuO1/jss8+qH/+///0v7bTTTrnSv9FGG6X33nuvsP0OAADQVrWp0P3GG2+kH374IVe062rXrl0O0k8++WTaYost0t1331193/PPP59DbATYDz74IO23335p7733Ti+//HI69dRTc9B97rnnqh8f/47A++ijj6Y55pgj7bHHHmnmmWdOzz77bHrggQfSm2++mS699NL0448/pp133jktuOCC+b4777wzffLJJ+moo47K2xk4cGA69NBD05577pleeeWVdMEFF6R+/fql/v3712p7hPoI0Jtsskk67rjj8oGECy+8MD399NM5pEd7llxyybT77runUaNGpT/++CMfeFhooYXya8R2I9wDAADQvNqnNuS7777LP//617/We/8ss8ySA2mE78svvzxXqeeZZ54cwCPQdujQId122205fK+zzjr5OVGB3nrrrdMtt9ySq+FhqaWWSgsvvHD+d4TlqEJHGO7UqVOadtpp02WXXZar1U888USaaqqp0hFHHJEqKytTx44d0wknnJCr599//32eZx2vtcEGG+RtLbbYYjns33TTTWnXXXfNt8W2I3CvttpqucIeotId7Yzq/dxzz51vO+CAA9Ltt9+eg/iMM86Yvv766xzup5566hy+d9ttt3TjjTcW/hkATEiMLGqN76e1vS+mXPok5Ui/pNz7ZFP7ZpsK3VFtDl999VWab775xrn/iy++yCG4S5cuOUDfc889OdxG9Tuq0KWQG9XhGFpeEh9ChPOa4b0kwnOE3AjcJXPNNVf+GcPVoxIegbvuffE6Q4cOTYsuumitNsb9cV/Ja6+9llZcccUc4GPI/PTTT5+GDRuWfv/993TIIYfkCn5JHFCI50bVPtoUIb+kZvsBWkpMuRkxYkRqbQYNGtTSTYBa9EnKkX5Ja+2TbSp0x5zqCN533HFHri7XFMG5tIJ3+/bt01ZbbZXOOeecHKC7du2aq8Eh5n1vttlm6ZRTTqlVQY/qckkM7y6Jx8cw8vgjshS8Iyi/8847ac4558wHAOK1S8E7qush2hn3l67XHEpeOngQogoe7dxuu+1S375981DxCNRRwb7++utz1b3k448/zvPY33///RzMf/vtt1x5D998800z7WWASbfIIouk1iS+3+M/7O7du9c6wAotRZ+kHOmXlHufLF2fVG0qdEcV+8wzz0wHHXRQ3nmxinkE2Aij559/fg6eMdc6xHDtWNTs//yf/5PncJfE0PMYih3Dy//+97/nUBxDvldfffV07LHHjvOaSyyxRK6qxynJjj766Bx0ow1RnY6542eddVY677zzclU6FlCLhdxiAbYI3HH/DjvskCvi8XpRAbrmmmvycPaa7yneS2wzDgYMGDAgB/FoZ7ync889Nx84iJXa+/Tpkw84xOJpsXr7aaedlk488cR80CACOkBLa61/bMX7aq3vjSmTPkk50i9prX2yTS2kFmLYeMx3jrAcoTbmZMfK4jG8OlYhn3322fPjotodq4ZHlTpWIi+JBcmimhyXnj17ph133DFXxw8//PB6Xy9CcZySLE5FFkE+5obH82L+defOnfPCaB9++GFaddVVU+/evXPYjkXYSq8V/46gHcPZDzzwwFzRjvbWFSuwx8GEqHbHa0XAj+fHgYV4biyoFnO8u3XrljtOHEyIsB0HDmKhtpg7DgAAQPOqqKo5LhoaKIZYxCrs70wzX/p6pC4ENM2snSrTbl1nTK31uzKm+qjeUA70ScqRfkm598mm9tE2V+kGAACAyUXoBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBB2he1YdqGmaauTGMrqlq6GcAUrktH/x0BAK2Tv3Jokg3m7ZwqKytbuhlAKzC2qiq1q6ho6WYAADQrw8tpkjFjxrR0E6C6L7733nv65BRM4AYAWiOhG2g1RowY0dJNAACAWoRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCN01SWVnZ0k1gCjS2qqqlmwAAAJNF+8nzMrRWAz4bnn4YLUDRcF06tk8bz9e5pZsBAACThdBNkwwbNSZ9O1LoBgAAqI/h5QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAcgzdQ4cOTX/++WfztQYAAADacugePXp0OuOMM9LSSy+dVlpppbTMMsukE044Id8OAAAANCF0X3nllenll19OF110UXrggQfyz7feeiv/pPmNGTMmDRkypKWbAQAAwCRo39gn3H///alfv35p7rnnztcXWGCBfNlhhx3SUUcdlcrBGmuskb7//vvUvv3/fXtVVVWpXbt2adFFF019+vRJ3bp1a9L277vvvnT11VenBx98sN77jznmmPzzrLPOSk112GGHpYUWWigddNBB9d6/yCKLpKmnnjpVVlaOc1+0b4455pjg9mPEwjXXXJOWXXbZvN8OPPDAtPnmmze53QAAAExC6P7555/T7LPPXuu2uD5y5MhUTvr27VsrPP7www/p+OOPz6Hy8ccfzyF8Um288cb5Mjn8+OOPE31MhObllltukrb/xhtvTNLzAAAAmLhGJ8+orN522221bovrCy+8cCpnf/3rX9M222yTvvzyy/TTTz9VB/Ejjjgirbjiinl++oknnph+/fXXfF8sEHfyySfn+yLQbr/99un111/P99111125KlzyxBNPpA033DAttdRSaZ999hknKEfFeaONNsrz3+NAwPPPP19930477ZTOP//8PFIgqs7rr79+GjBgQL4vqvKvvfZarqrvu+++k/S+L7744rTtttvWuu3cc89Ne++9d/XnGdMFAAAAKINK96GHHpp23333PMQ6hph//vnn6aOPPkrXXXddKmdff/11uvnmm1P37t3TTDPNlMaOHZv233//NN9886VHHnkk/fHHH+nYY4/NwfuCCy5I9957b64CP/TQQ2naaadNl1xySa6ex/uu6eOPP06HHHJIXlxugw02SE8//XQ6+OCDqyvhzzzzTDrppJPyXPgePXqkZ599Ng8Vv/322/Ow8RD/jiH7Cy64YLr88stzG9Zcc810+umn5/3bq1ev8Q4vn5gtt9wyXXXVVenTTz/N7zXmiMd7iMXvoCVFXyxie829XWgK/ZJyo09SjvRLyr1PNrVvNjp0x9zfe+65Jy+iFpXitddeOy+iNuecc6ZyEgE5gnBUrCNQzzbbbLmtUYkO77zzTnr33Xdz2I1QHY4++ui03nrr5UDasWPH9MUXX6Q77rgjrbLKKjlYx/zquqIqvfjii1eH7LXWWiutvvrq1fdH0N9uu+1Sz5498/W4L6rkMTqgFHzXXXfd6nnmm222WQ7JcTq2ic3HLokqeN053VFVjwp5fC5///vf82cWB0yiyh6dpmYboSUMHjw4jRgxotm3O2jQoGbfJjSVfkm50ScpR/olrbVPNjp0n3baaXludFRza4pF1M4555xULqK6HEO541Rm/fv3z0F21VVXTTPOOGO+PwJ1hM+4raYOHTrk1cJjuHiE9X//+9+58t2lS5ccbiNA1/Ttt9+OE47nmWee6iHmMZz9lVdeSf/85z+r74/XXX755auvzzzzzNX/Li3+FpX4hor3NqE53VtttVX+bOLAwd1335022WSTNNVUUzV4+1CEmNrQnOL3Kr4YYzRLfQsLQkvQLyk3+iTlSL+k3Ptk6XqhoTuC5UsvvZT/HSE0Krs1DR8+PD322GOpHEWI3nPPPfMCcDGcPMJv165dc+U7qtkxn7n0yx0BPQL3vPPOmz755JO02GKLpU033TQvEvfwww/nSnhU+muK7cSQ8pq++eabvKJ46f7YRmkOdfjqq6/ya08uMVQ9Kv8xtP3JJ5/MwRtaWlH/qcZ2/YdNudEvKTf6JOVIv6S19skGLaQW1eEYJh3zmiOYxs+al1tvvTWvCl7OYmh1VNb+8Y9/5BC9xBJL5HAdp/X67bff8m0xHH3XXXfNRzKeeuqp/J6iIh4BeYYZZshV6M6dO9fabgwr//DDD/O87BjKHsO3ax6A2HrrrXOl/e23387X4whJVOBjeH5DDxrEQY2miKp2BP8I3nEgIU7xBgAAQPHaNzT4xdzmsMcee5T9omn1iSMUsWp3hM+zzz47Dz+POc/x73XWWSeNGjUqB/GY4x1V6p133jlX+GPl71jRPOZGX3jhhblyXVMsJhfDuyO8x8JnEWpj7nhJzBH//fff03HHHZcr3BHeI9jHquUNEe2NVdRjDnoc3KjPXnvtVe8RmGhPLO5WGmJ+/fXXpwMOOKCRew4AAIBJVVFVVVU1yc+mzYrRAG+++WZ6Z5r50tcjdSEabtZOlWm3rv93bYUi+mScus/QNMqFfkm50ScpR/ol5d4nm9pHG72QWsyHrqioqPe+999/v9ENAAAAgNaq0aE75ifXNGzYsHTTTTflFbEBAACAJoTuXr16jXNbnBM65inHomEAAABAI1Yvn5jpppsuLzoGAAAANKHSfc8999S6/scff6QnnngiLbrooo3dFAAAALRqjQ7dcV7ummL1tjjvc5yCCwAAAGhC6H7yyScb+xQAAABokxocul999dWJPqZnz55NbQ8AAAC0vdC900475Z81z9E9/fTTp+HDh6exY8emGWaYIb300kvFtBIAAABac+j+4IMP8s/rrrsuffjhh+n4449PnTt3Tr///ns666yzcgAHAAAAmnDKsAjdffv2zYE7TDPNNKlPnz7p9ttvb+ymAAAAoFVrdOiOoeRDhw6tddsXX3yRVzEHAAAAmrB6+SabbJL22GOPtOeee6bZZ589DRkyJF177bVp2223beymaAVmmroyja2oaulmMAXp0rHRXzsAADDFavRfv0ceeWQeUn7llVemb7/9NgfvrbfeOu21117FtJCytsG8nY1yoNHGVlWldjUWZQQAgNaq0aG7ffv26ZBDDskXGDNmjNBNowncAAC0FY2e011VVZVuvPHGtMEGG6Qll1wyrbXWWumqq67KtwMAAABNqHT3798/9evXL+29995prrnmSp9//nme092uXbt8GwAAADCJofu2225LV1xxRerWrVv1bT169EgHHXSQ0A0AAABNGV7+3Xffpa5du9a6La7/9NNPjd0UAAAAtGqNDt3zzjtveuyxx2rdFtfjdgAAAKAJw8v333//dOihh6aHH344zT333HlO9xNPPJEuueSSxm4KAAAAWrVGV7pjtfJYOK1Dhw7p3XffTdNNN1265ZZb0uqrr15MCwEAAKCtVLr322+/dO6556bll1++mBYBAABAW610v/HGG7nKDQAAADRzpbt3797p4IMPThtttFGaeeaZU0VFRfV9PXv2bOzmAAAAoNVqdOi++eab88+nn3661u0Rvt9///3maxkAAAC0tdD9wQcfFNMSAAAAaMtzul9++eV0ww03CN4AAADQnKH7nnvuSbvttlu66qqr0pZbbpkef/zxhj4VAAAA2qQGh+6rr746nXfeeWngwIHpuOOOS9dff32xLQMAAIC2Erq/+eabtMEGG+R/b7755unjjz8usl0AAADQdkJ3u3b/76EdO3ZMY8eOLapNAAAA0LZCd1VVVbEtAQAAgLZ6yrAI3V9//XV1+I5Kd83rYY455iimlQAAANCaQ/eIESPSGmusUX09wnbpevy7oqIivf/++8W0EgAAAFpz6H7iiSeKbQkAAAC01dA955xzNnijG220Ubr//vsntU0AAADQthZSa4wvvviiiM0CAADAFKWQ0B3zuwEAAKCtKyR0AwAAAEI3AAAAFEboBgAAgIII3QAAADAlhe6qqqoiNgsAAABtI3S/99576dFHH02jR49OQ4cOrXVf//79m6NtAAAA0LZCdwTsbbfdNm299dbp6KOPTkOGDElrrbVWeuONN6of07179+ZuJwAAALT+0H3GGWekhRdeOL366qupffv2aYEFFkh77713Ouecc4ppIQAAALSV0D1w4MB07LHHpk6dOqWKiop825577pk++uijItoHAAAAbSd0TzXVVGnkyJG1Fkz77bff0rTTTtv8rQMAAIC2FLrXWGONdOSRR6ZPP/00V7pjjnffvn3TqquuWkwLAQAAoK2E7sMPPzxNM800ab311ku//PJLWmmlldKIESPSEUccUUwLAQAAYArVvrFPiGHkl1xySRo2bFj64osv0myzzZZmmWWWYlpH2ausrGzpJrRJY6uqUrv/f00FAACgFYXu8Nprr6Uvv/wyz+n++OOPq2/fdNNNm7NtTAEGfDY8/TD6/87tZ/Lo0rF92ni+zi3dDAAAoIjQfdJJJ6U77rgjV7dLq5eH+LfQ3fYMGzUmfTtS6AYAAGiW0D1gwID0r3/9Ky2++OKNfSoAAAC0KY1eSK1z585p4YUXLqY1AAAA0JYr3fvtt1/q06dP2mOPPdJ0001X67455pijOdsGAAAAbSt0jxo1Kg8xf+CBB6pviwXVYk73+++/39ztAwAAgLYTuq+44op0/PHH5/Nzt2vX6NHpAAAA0GY0OnSPGTMmbbfddsW0BgAAAFqRRpeqN99889S/f/9iWgMAAABtudL99ttvp379+qWLL744TT/99LXO1f3EE080d/sAAACg7YTuLbfcMl8AAACAZg7dm222Wf45dOjQ9OWXX6aZZ545zT777I3dDAAAALR6jQ7dv/76azr66KPTk08+WX2qsBVWWCFddNFF45y3GwAAANqyRi+kdv7556fffvstn6f7rbfeSvfee28aO3ZsOvfccxu8jTXWWCN17949Lb300uNcXnvttYk+/6uvvsqPjZ/l5tJLL0077bTTJD33mGOOSYssskjex3XFyILFF18877tJFc+96667Jvn5AAAAFFzpfuqpp9Kdd96ZunTpkq8vvPDCOXBvvPHG6dRTT23wdvr27ZtXQp8Uc8wxR3rjjTdSazTjjDPmAxmHHXZYrfOg33PPPWnqqadu0bYBAABQcKV7xIgRqXPnzrVui2HlUe1uTlGVvfrqq9Omm26aq9rxc+DAgfm+L774IleE42fp+h577JF69OiR1ltvvXTDDTfk+8PLL7+ct3XttdemFVdcMS2zzDLpggsuyCutr7vuunnbBx10UBo9enR+/LfffpsOPfTQ/Jwll1wyrbnmmumOO+4Ybzv/85//pC222CIttdRSadttt61uU8njjz+eDy5E2+L1om0T2lfRxj/++CO9+OKLtW6PCvWGG25Y67Z33303V9V79uyZ1llnnbztGPIf4udVV12VVlpppbTsssums88+O59jvWTkyJHpnHPOSauuump+fmwnVqYHAACgBUN3BNE4XVjNcBfXY7h4c4uKemw7AmjXrl3TySefPM5jIkjus88+aZZZZknPP/98uu6663JVuKZY8O37779PTz/9dA7cEeZvueWWdPvtt6f77rsvB/MBAwbkxx5//PFpqqmmSg8++GAO1DvuuGOu4MeQ+rp+/PHH/NoRpl999dV05JFH5pBdEgcJIsDvueee6ZVXXsmvHadbm9B5zuO1e/fune6+++7q29588828nyPYl8TBgV122SUfZIj9c8UVV6Rbb701/etf/6redzfeeGN+r3F/bPebb76pfn7sy9hf0ZYXXnghrbXWWmnXXXctyyH7AAAAbWZ4+RFHHJGrohFW55xzzhxoYzG1CJONEcPLzzjjjFq3xSro999/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iNA9BRk1alT65ptvWroZAAAANJDQ3Ug///xzOvnkk9Oqq66allpqqbTSSiulo48+ulYY3nDDDdN9992X/73TTjulSy+9tFlee/vtt08vvvhivfd98cUXaZFFFsk/6zrmmGPyJUS7on3h5Zdfzs+Z2PMBAACYNEJ3Ix122GHpxx9/THfccUd688030z333JNGjx6ddtttt/Tnn3/mxzz44INp4403bvbXjtdtqmhXtA8AAIDiCd2N9Prrr6e11147zTzzzPn6X//613TcccelJZdcMv3yyy/5tjXWWCPddddd4zy3qqoq9e/fP6277rpp2WWXzZXrd955p/r+eN7VV1+dNt1007T00kvnnwMHDsz37b777umrr75KJ510UjrllFMmuf3RrngdAAAAitd+MrxGqxJDsyP4vvbaa6lXr145bM8555zprLPOmuhzb7311tSvX7905ZVXpgUWWCDde++9uUL+0EMP5fAe7rzzznTNNdekWWaZJfXt2zcPZX/44YfT9ddfn8PygQcemDbffPMJVrLbtat9LGXkyJGpd+/ezfDumZAxY8a0dBPatNL+9zlQTvRLyo0+STnSLyn3PtnUvil0N9Jpp52WlltuuTRgwIB04oknpuHDh6d55pknHXTQQRMdUn7LLbekffbZJ3Xt2jVf33LLLfMw9ZhnHZXs0m3zzjtv/vdGG22Uh683RmxrrrnmqnVbaT43xRo8eHAaMWJESzejzRs0aFBLNwHGoV9SbvRJypF+SWvtk0J3I0UVeZNNNsmXGC7+v//9L1esjzrqqDzkfIUVVhjvc7/88st09tlnp/POO6/6tpgHvvjii1dfL1W8Q/v27fNrMGUoLUpHy4gjkPHF2L1791RZWdnSzYFMv6Tc6JOUI/2Scu+TpeuTSuhuhOeeey4dfPDB6amnnkozzDBDqqioSAsuuGA6/PDD0wsvvJDee++9CYbu2WabLT+/tHp4+Pzzz/O2mPL5T6J8PgefBeVGv6Tc6JOUI/2S1tonLaTWCD179kxdunRJxx57bB5K/Mcff6Rff/01D+n+9NNP02qrrTbB52+99dZ5PndUx0shPgL4q6++2qDX79ChQx7ODgAAwJRBpbsROnbsmBdDu+yyy9J+++2Xhg4dmqaaaqp8vu5YIC0WR5uQXXfdNQ8X33///dN3332XZp111jwvfM0112zQ68d87wsvvDAPbag5RB0AAIDyVFFl0jCTIOY1xHnK35lmvvT1yLbdhWbtVJl26zpjSzejzSv1yTgIZmga5UK/pNzok5Qj/ZJy75NN7aOGlwMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIO2L2jBtw0xTV6axFVWpLevS0a8RAABQP2mBJtlg3s6psrIytXVjq6pSu4qKlm4GAABQZgwvp0nGjBnT0k0oCwI3AABQH6EbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURummSysrK1NaMrapq6SYAAABTiPYt3QCmbAM+G55+GN12QmiXju3TxvN1bulmAAAAUwihmyYZNmpM+nZk2wndAAAAjWF4OQAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3VT79NNPW7oJAAAArYrQPQkWWWSRfPn444/Hua9fv375vksvvTRfP/HEE/Ol3Hz33Xdpyy23TEsttVQ64ogj0i233JJOOOGElm4WAABAq9K+pRswpZpxxhnT3XffnQ4//PBat991113pL3/5S/X1U045JZWjgQMHpi+//DK98sorqUOHDtUHCQAAAGg+Kt2TaKONNkr33ntvGjt2bPVtb7/9dho9enTq1q1b9W3HHHNMvoQItgcffHCuLC+77LJplVVWSeeff371Y+O5F198cVpzzTVTr1690l577ZU+++yz6vuHDBmS9t1337TMMsukFVZYIZ188sn5OV988UWurp911lmpZ8+eqW/fvvn2s88+O62//vpp6aWXzo8/9dRTU1VVVerfv3/q06dP+vHHH9Nyyy2XDx5cffXV6bXXXsvtAgAAoHkI3ZNotdVWS3/88Ud68cUXq2+744478pDtCXn00UfTSiutlF5++eUcgq+55pr05ptv5vsuvPDC9PTTT6cbbrghPffcc2nJJZdMu+++exo1alT6888/0x577JFmnnnm9Oyzz6YHHnggP69mhfq3335LL7zwQjrssMPSjTfemLcRP9944410xRVXpNtuuy1XuHfeeecczOeYY45832abbZb22WefHLgjeAMAANA8DC+fRO3bt8/V7qgSR4geOXJkeuSRR3IYjlA8PvPNN1/adNNN879XXXXVHKJjAbMI2BGKL7nkkjT33HPn+w844IB0++235yAew9ljOPhxxx2XOnXqlKaddtp02WWX1aq0x3ZjqHhctt566xymu3TpkudvR/viOd9+++1k2Dut35gxY1q6CYznM/HZUE70S8qNPkk50i8p9z7Z1L4pdDfB5ptvnrbZZpv066+/pscffzz16NEjh+gJqXv/VFNNlYPzsGHD0u+//54OOeSQ1K7d/xuAENX0CNtR6Y7gHYG7ZK655so/Y3h5mGWWWarvGzFiRJ5P/uqrr6bZZpstD3mPoeU1QzqTbvDgwXkfU34GDRrU0k2AceiXlBt9knKkX9Ja+6TQ3QRdu3ZN888/f3rooYfS/fffn3bZZZdJ3lYE6qmnnjpdf/31eUXxklghfdZZZ00ffPBBnoMdQa8UvGMo+DvvvJPWWmutfL2ioqL6eccff3yafvrp0/PPP5+3G2E75nvTPGIOPeUljkDGF2P37t1TZWVlSzcHMv2ScqNPUo70S8q9T5auTyqhuxmq3TEH+5dffsnDxSdVVLdjPngsrHbuuefmqnUs1BYLnsVc8SWWWCIPTY/F0Y4++ug8f/vMM89MK664Yr3bi+p7bCO2G/+OoejxMyrn9YlgHvdHNbxmeKd+/kMo78/G50O50S8pN/ok5Ui/pLX2SQupNVHv3r3zCuMbb7xxnufdFBGmY2739ttvnxc1izAfc7xjaHgMQ7/qqqvynOxYxG2TTTbJletYDb0+UemO6nisgr7eeuvlQL3yyiunDz/8sN7Hr7766umnn37KK6PHAQQAAACarqIqSpvQSDHEIlZPf2ea+dLXI9tOF5q1U2XareuMLd0MJtAnY3qGo+SUC/2ScqNPUo70S8q9Tza1j6p0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAg7YvaMG3DTFNXprEVVamt6NLRrwwAANBwEgRNssG8nVNlZWVqS8ZWVaV2FRUt3QwAAGAKYHg5TTJmzJjU1gjcAABAQwndAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEBBhG4AAAAoiNANAAAABRG6AQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0E2TVFZWtsjrjq2qapHXBQAAaIz2jXo01DHgs+Hph9GTNwB36dg+bTxf58n6mgAAAJNC6KZJho0ak74dqeoMAABQH8PLAQAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3S1kzJgxaciQIS3dDAAAAAo0RYXuE088MS299NL50r1799S1a9fq63F57bXX0jHHHJMvzeGLL75IiyyySP7Z3A477LB0zz33TNJzq6qq0uGHH56WWmqptMYaa+TrNd1111359vrE7XE/AAAAxWufpiCnnHJKvoQIjpdddll68sknaz3mjjvuSFOCH3/8cZKf+91336UHHngg74PFFlusWdsFAABAG610N9TQoUPTwQcfnJZbbrm00korpZtvvrn6vl9//TUH91VXXTWtsMIKueL8ww8/TNLrxLaOP/74tM466+Sq88orr5yuuuqq6vsfeeSRtOGGG6Zlllkmrb/++umKK67It/fp0ydX5a+++uq077771rvtuH+HHXZIyy67bK5OX3TRRWn06NHpvffeS+uuu25+TNx/ySWXpEn13//+N2+jZ8+eafXVV09HH310fk8AAAC0wUp3Qw0cODAH2osvvjgP4T722GPT2muvnWadddZ03HHHpd9++y1XiTt27JjOOuusdOCBB6Z//vOfqaKiolGvc9555+Wh51Fd79y5c3r00Udz2I+AHa915JFHpmuuuSaH/wjLEXDjIMDpp5+ePv/889SrV6900EEHjbPdjz/+OO22227piCOOSP369Utff/11flwp5EeVe80118w/55prrkneT3379s0HHuKgRFTed9lll/Tvf/87v/aUMi8e6vYH/YJyol9SbvRJypF+Sbn3yab2zVYZuldcccX097//Pf87Ks0xxzsWLWvfvn2uPj/00EOpS5cu+f4I4VFNfvfdd9Piiy/eqNeJIFxZWZn+8pe/pG+++SZNPfXU1cO/I3RHqI9APnbs2NSjR4/0+uuvp3btJj644P77789zySMEh3nnnTfP4Y5AH+1tLtHe5557Li2wwAI5fN97770Nal+5GDx4cBoxYkRLN4MyM2jQoJZuAoxDv6Tc6JOUI/2S1tonW2XonmGGGar/3aFDh+qjE19++WX+99Zbb13r8RGco2Ld2NAdw9ijah1V7Kg4l54fITsCd1TPY0h5BOaoUsew8KhUTz/99BPd7txzz13rttj+yJEj830NCdN//vlnvffF7aWDAzFk/dJLL00XXnhh+sc//pEPDJx88slpoYUWSlOCODABJfE7Hl+Mschi/E5DOdAvKTf6JOVIv6Tc+2Tp+qRqlaF7fKL6HKLSPfPMM1ff/tFHH40TchvikEMOyfOtr7vuulxFjyHat99+e74vQnZUvM8///x8/f3338/BNuZ8x9zpCZlzzjnzUPWaYjh6HECIwB7bnZDZZpstDRs2LIf0CP8lMaw+5q/PMccc+cBAHCyIan1Uz2MI+5lnnplHBdx5551pSuBLmfH1C32DcqNfUm70ScqRfklr7ZNTzljiZgrdq622Wq5OR0D+448/0pVXXpm23HLL9Msvv4z3eRFUY/h4zUsYPnx4DrXxQUTIPe200/Ltsd0IuHvttVceKh6n9Jplllny0O0ZZ5wxPyYCdDy/PjEk/n//+1+68cYb8+JpEbgvuOCCtNFGG1VX7idkySWXzME95mxHu8K3336bF5Cbf/750xJLLJHbEu2NaveoUaPSTDPNlCvgpfYBAADQdG0qdIdzzjknTTfddGnTTTdNyy+/fHrmmWfStddeW6vyXdc222yTVzuveYmgGpXhAQMG5GHZm2++eQ713bp1Sx9++GH+d6wsHgupxf29e/fOr7frrrvmbcbrR0V5++23H+f1Yih5tCnmn8fc9HhMzFOP85Q3RFTdYwG2COwbb7xxXll9iy22yPfF7aWjNRG4I9zH4m7xOnEQ4NRTT53EPQsAAEBdFVVRhoVGinkNb775ZnpnmvnS1yMnbxeatVNl2q2rijz198k4yGRoGuVCv6Tc6JOUI/2Scu+TTe2jba7SDQAAAJOL0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUpH1RG6ZtmGnqyjS2omqyvmaXjrotAAAwZZBeaJIN5u2cKisrJ/vrjq2qSu0qKib76wIAADSG4eU0yZgxY1rkdQVuAABgSiB0AwAAQEGEbgAAACiI0A0AAAAFEboBAACgIEI3AAAAFEToBgAAgIII3QAAAFAQoRsAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAArSvqgN07pVVVXln2PGjMkXaGmlfqg/Uk70S8qNPkk50i8p9z5Z+lnKQI1VUTWpz6RNGz16dBo0aFBLNwMAAGCy6N69e+rQoUOjnyd0M0nGjh2b/vzzz9SuXbtUUVHR0s0BAAAoRETmyD/t27fP+aexhG4AAAAoiIXUAAAAoCBCNwAAABRE6AYAAICCCN0AAABQEKEbAAAACiJ0AwAAQEGEbsZr6NChaf/990/LLrtsWm655dLpp5+ez81dn2eeeSZttNFGaamllkrrr79+euqppyZ7e2n9GtMn99xzz9S9e/e09NJLV1+effbZyd5m2o5hw4altddeO7388svjfYzvSsqtT/quZHL44IMP0m677ZZ69eqVVlxxxXTUUUfl/lkf35OUY79s8ndlnKcb6rPjjjtWHX744VW///571eeff1614YYbVl1zzTXjPO6TTz6p6t69e9Vjjz1W9ccff1Q9+OCDVUsssUTVN9980yLtpvVqaJ8Myy23XNXLL7882dtI2/Taa69VrbXWWlULL7xw1cCBA+t9jO9Kyq1PBt+VFG3EiBFVK664YtXFF19cNWrUqKphw4ZV7bXXXlX77LPPOI/1PUk59svm+K5U6aZen332WXrllVfSkUcemTp16pTmnnvuXGG85ZZbxnns3XffnSuPa621Vmrfvn3aYIMNUs+ePdO//vWvFmk7rVNj+uSQIUPSzz//nLp169YibaVtie/AI444Ih122GETfZzvSsqpT/quZHL46quvUteuXdMBBxyQOnTokGaccca0zTbbpFdffXWcx/qepBz7ZXN8Vwrd1Ou///1vmmGGGdKss85afdsCCyyQO+gvv/xS67EfffRRWnjhhWvdtuCCC+YhG9ASfXLQoEFp2mmnzX9wLr/88ql3797pjjvuaIFW0xastNJK6bHHHst/HE6I70rKrU/6rmRymH/++dO1116bKisrq2975JFH0mKLLTbOY31PUo79sjm+K9s3S6tpdX777bdcTaypdP33339P00033QQf27Fjx/w4aIk+OXr06DwXLL4cF1pooTyf8aCDDspfmDE/DJrTzDPP3KDH+a6k3Pqk70omt6qqqnTRRRfledo333zzOPf7nqQc+2VzfFcK3dRrmmmmSSNGjKh1W+l6dLCa4stx5MiRtW6L63UfB5OrT2666ab5UrPqE9cfeughf0jSYnxXUm58VzI5/frrr+nYY49N7777bg42iyyyyDiP8T1JOfbL5viuNLycesVRnJ9++in98MMP1bf973//S7PNNlvq3LlzrcfGMKAY+lt3eFBsA1qiT8aQn/girHuUcuqpp55s7YW6fFdSbnxXMrl8/vnnaYsttsgBJ/pdfcEm+J6kHPtlc3xXCt3Ua7755kvLLLNMOuOMM3JHjAUErrjiirTllluO89iNN944L3A1YMCAfPqm+BnXN9lkkxZpO61TY/pk3H/qqaem9957L40dOzY9/fTT6YEHHsgLZEBL8V1JufFdyeQQC1DtsssuqUePHum6665LM80003gf63uScuyXzfFdWRFLmDdT22lloqJ4yimn5HkL7dq1y8MoYjXUWHAgzk3Xt2/f/OUYnnvuuXTeeeflI0ZzzjlnXmF61VVXbem3QBvtk/G1duWVV+Yjk3Fu71jp/MADD0zrrbdeS78FWrk4St6/f/98Hvngu5Jy7pO+K5kc+vXrl84666w8dLyioqLWfW+88YbvScq+XzbHd6XQDQAAAAUxvBwAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAtCrDhg1La6+9dnr55Zcb/JxHHnkk9e7dOy211FL5uXfccUeztKV9s2wFAGgTqqqqUkVFRUs3AwDG6/XXX0/HHHNM+vzzz1NDDRw4MD/noosuSqusskoO63vttVdaeOGF0xJLLJGaQqUbAMrIm2++mf7xj3+k1VZbLf8nv+aaa6bjjz8+/e9//2vppqV///vf6eyzz66+ftddd6VFFlkkffHFF+N9TtwXj4nHNtWll16at9UUsS+7deuWvv/++/E+Zv/9908rrbRSGjNmTCpS3fcTf+ytscYaE3xOQ/Y5QFt29913pyOOOCIddthh49z34osvpi233DItu+yyacMNN0z33Xdf9X033HBD2nnnndOqq66aDy4vv/zy6c4770zzzDNPk9skdANAmbjuuuvSdtttl3755Zd05JFHpmuvvTbtu+++6b333kubbbZZevDBB1u0fVdeeWX66aefqq/HgYF//etfaZZZZklTivhjK8L0+Pbljz/+mJ599tm0+eabp8rKysnatgj7l1122WR9TYDWZqWVVkqPPfZY2mCDDWrd/sEHH6T99tsv7b333rmKfeqpp6YzzjgjPffcc/n+t99+O80wwwz5/uWWWy5tsskmuVIetzWV0A0AZeD5559P5557bg7ZEbbjCHyvXr3SVlttlYNtBNyohP73v/9N5WKmmWbK8946dOiQphTR3gUXXLBWdaOmBx54IP355585nE9uUU2JKjwAk27mmWdO7duPO4v6tttuy6PH1llnnXxQtUePHmnrrbdOt9xyS77/559/zge/I5i/8MIL6YADDsjV8rfeeis1ldANAGXg8ssvT3/729/SwQcfPM59U001Verbt2/+I+Gaa66pvj2GIkcQn9jw48cffzxtv/32aemll06LL754Wm+99dLNN99cfX8c8Y/nvPTSS2n33XdPSy65ZPr73/+eh5JHAC291pdffpmH7ZW2X99rPfroo2njjTfOQ+OjOh+VhbritgMPPDAP3VtsscXSyiuvnE477bQ0cuTI6seMGjUqnXnmmWnFFVfM7T722GPzbXW99tpraccdd8xtjoMURx99dF48Z0K22GKL9O6776aPP/54nPvi/cV2SsMJP/zww7TPPvvkP87iEn+EDRkypFH7rqHvp+7w8rFjx6YrrrgiH3CJ7UYlPP4orGtiny8AKf8fFhXwGFpeutx0003p66+/zvfHAeT4/yG+SyO0RzhfYYUV8uJqTSV0A0ALiyHNb7zxRj4CP75FymacccYc5p544olGbfvpp5/OQTHCbQS4mEc855xz5mF1//nPf2o9NubALbPMMumqq65KG220Ubr++uurV26NYc9RPYi5buMbUv7kk0/mgwYLLbRQfvz666+fh8nX9N1336UddtghjRgxIp111ln5IEI8Lv7wifl0JfG8eJ1YxCYWtYmwWfP+8Oqrr6Zdd901dezYMT/muOOOS6+88kqek1czwNe16aab5gMZdavdH330UQ7jpSr3J598krbddts0dOjQ3NbTTz89B+6YAhC3NXTfNfT91BUjH+JgTPwRGPsz+sD5558/yZ8vQFs222yz5YPBcbC2dIlA/X/+z//J9y+wwAJp9OjRtZ4T05FiAdGmEroBoIV99dVX+T/1CEsTMu+886Zff/211rzqiYkgGSGzT58++Yj96quvXh3cIrTWFEPZI8DF46ISO9dcc+VQF2LYc1QBJjSkPAJihL/Yfqz8GvPiYpheTVE5XnTRRdPFF1+cK7hxICHCcqwOW2pPDKGPP4QiqEaojqAfoTPef03xOjE64Oqrr87vK95nhN2oYMfiN+MT7yFeO4aS161yTz/99GndddfN1+M1I9BHOI6KRxwc6N+/fw70MQWgofuuoe+nppjXHwci4gDCQQcdlEcDROiP0QGT+vkCtGVbbrll/t6P6VwxkujTTz/NI6Xi/40QB1T/+c9/5sXW4v743o7RTHEKsaZyyjAAaGGlo+gTOxVX6f74Y6Ch9txzz/zz999/zwvCRPV20KBB+bY//vij1mNjSF3dqkA8ryEiiEaVuO7w+AiqNauzscBNXOK1oy3xR8/gwYPzkPDSYjVRfQhR+S9p165dDsMRMkNUymOe3R577JH3X2ko99xzz52rFTEfLyrqE/rjK4aNRzU4ho3HPr3//vtzlXrqqaeuPn1MLKYTwbu0/b/85S95SGL8UdbQfdeQ91PfKvaxj2o+p7Q/S4v+NPbzBWjLllxyyXTBBRfkyyGHHJI6deqUA3WcMSTEqKL4bo6pQDFtKg6EX3jhhflgclMJ3QDQwuaYY478s+Zc4frEHwHTTDNNo1ZSjTB70kkn5Xm/EdqjuhrDoEPdIXMRLmuKPz4aOqwuhkvHY6OKXFPdYegRbuMPnli4JoLi7LPPnud/l4JuaVuh7rZieHvNSnBsK4an15znXlJze/WJyvGss86ag3aE7gjR3377ba0F1GJEwYABA/Klrrptm9C+a8j7qauhz2nM5wvQ1gwePLjW9RjlFJfxieHncWluQjcAtLAIVlEpjeB0+OGH58BWCl4RLqN6O3z48BwMo0pcuj/UPZd03cp0zDWOc3z369cvh8sYFh5V4jjndnOKAwHRrh9++KHW7XWHwsfcuRiuffLJJ+dKb+fOnfPtNcNuzF0Osa3SAYm625p22mlzyIzh2rHSe11RwZiQWJQuhmXffvvteWj2Pffck6sZMfS9JNoWw9932223cZ5f38q449OQ9zO+58Tc8fnnn3+8z5lcny8Ak86cbgAoA7Ga92effZbnOpfEvLOYSxyrWp944ok5TMUpxUpiqPM333xTazt1F896/fXXc7iNucCledhxHurGDlMPNcN+fZXlOHAQq5fXrLDG4mp12xOn7IqQXQrcUWGOud6l9pTmLT/88MO1nvvUU0/Veu8xzzzmb3fv3r36UlrELebhTUwMJYwQG/s52hnzsmuKVcxj+HcE8dL2Y3XwOGgQK+A2VEPeT12xL6N6PrHnNOfnC0AxVLoBoAxEBTtOd3XOOeek9957Lw9vi+HPsZBWaZXrzTffvNbcslg0KxYRixWzY3GzWLgrTl1VUwzdjiHU8byYZxyrpMdzokocIb4xpptuuty2WCE8tltXzIvbZZdd8gGEbbbZJs/XvvLKK8dpT6yyHRXvaHMcaIj2xIqxpfbEEOl4fsyli7nUEXrvvffecYYJxuvFYm0xOiBOUxZV/1gQJ+Z6113ArT7xOj179szz9+K5dRfLiVN0xerlMfc7FtiJAwuxAnmMSLjkkksavN8a+n5qikp+vH6sdB5V+wjVzzzzzDihuzk/XwCKodINAGUihjHfeuutOXDFKarielSOYxh0rGD90EMP5VBbOi92hMGozkbQjJAZFeNY4bqm2E4sHhOnkIrVtSMwxjm/I+SXFvhqqDgPdQyRjsXL3nnnnXHujwXGYn51tCOC92233ZbOOOOMWo8pBdhYBTxOn3XdddelTTbZJD8+VvkuzWWOecpxf5xvOu6LhdpqVvlDvId4flT7YwG3o446Kg8bj6HWEegbIqrdcXAgzm1dqryXdO3aNc89jwAb247X+P777/Mq7TECoTEa8n7qin0VK7tHtTs+3wjpcWCmqM8XgGJUVFllAwCmmFOLxWmkIrRFMAcAyp/QDQAAAAUxvBwAAAAKInQDAABAQYRuAAAAKIjQDQAAAAURugEAAKAgQjcAAAAUROgGAACAggjdAAAAUBChGwAAAAoidAMAAEAqxv8HeiRNPD1CSDoAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_style(\"whitegrid\")\n",
    "plt.figure(figsize = (10, 7))\n",
    "top_10_produtos.sort_values(ascending = True).plot(kind = 'barh', color = 'skyblue')\n",
    "plt.title('Top 10 Produtos Mais Vendidos', fontsize = 16)\n",
    "plt.xlabel('Quantidade Vendida', fontsize = 12)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d1b4c1f1-c87c-4161-bf42-e044b74dba02",
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
       "      <th>ID_Pedido</th>\n",
       "      <th>Data_Pedido</th>\n",
       "      <th>Nome_Produto</th>\n",
       "      <th>Categoria</th>\n",
       "      <th>Preco_Unitario</th>\n",
       "      <th>Quantidade</th>\n",
       "      <th>ID_Cliente</th>\n",
       "      <th>Cidade</th>\n",
       "      <th>Estado</th>\n",
       "      <th>Faturamento</th>\n",
       "      <th>Status_Entrega</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>2026-01-01 03:00:00</td>\n",
       "      <td>Hollow Knight</td>\n",
       "      <td>Indie</td>\n",
       "      <td>7500.00</td>\n",
       "      <td>4</td>\n",
       "      <td>109</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>30000.00</td>\n",
       "      <td>Rápida</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>2026-01-01 06:00:00</td>\n",
       "      <td>God of War</td>\n",
       "      <td>Ação</td>\n",
       "      <td>4500.00</td>\n",
       "      <td>5</td>\n",
       "      <td>148</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>BA</td>\n",
       "      <td>22500.00</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>2026-01-01 08:00:00</td>\n",
       "      <td>Minecraft</td>\n",
       "      <td>Indie</td>\n",
       "      <td>549.61</td>\n",
       "      <td>2</td>\n",
       "      <td>141</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>1099.22</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>2026-01-01 09:00:00</td>\n",
       "      <td>Resident Evil</td>\n",
       "      <td>Apocaliptico</td>\n",
       "      <td>1200.00</td>\n",
       "      <td>4</td>\n",
       "      <td>121</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>4800.00</td>\n",
       "      <td>Rápida</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>2026-01-01 16:00:00</td>\n",
       "      <td>Overcooked</td>\n",
       "      <td>Indie</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>1</td>\n",
       "      <td>110</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID_Pedido         Data_Pedido   Nome_Produto     Categoria  Preco_Unitario  \\\n",
       "0       1000 2026-01-01 03:00:00  Hollow Knight         Indie         7500.00   \n",
       "1       1001 2026-01-01 06:00:00     God of War          Ação         4500.00   \n",
       "2       1002 2026-01-01 08:00:00      Minecraft         Indie          549.61   \n",
       "3       1003 2026-01-01 09:00:00  Resident Evil  Apocaliptico         1200.00   \n",
       "4       1004 2026-01-01 16:00:00     Overcooked         Indie         2546.30   \n",
       "\n",
       "   Quantidade  ID_Cliente          Cidade Estado  Faturamento Status_Entrega  \n",
       "0           4         109  Rio de Janeiro     RJ     30000.00         Rápida  \n",
       "1           5         148        Salvador     BA     22500.00         Normal  \n",
       "2           2         141        Curitiba     PR      1099.22         Normal  \n",
       "3           4         121  Rio de Janeiro     RJ      4800.00         Rápida  \n",
       "4           1         110        Curitiba     PR      2546.30         Normal  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "943d56ad-f84f-4815-a2eb-782826a37fc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1d16dd32-3b2e-413c-81e9-208aee3be074",
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
       "      <th>ID_Pedido</th>\n",
       "      <th>Data_Pedido</th>\n",
       "      <th>Nome_Produto</th>\n",
       "      <th>Categoria</th>\n",
       "      <th>Preco_Unitario</th>\n",
       "      <th>Quantidade</th>\n",
       "      <th>ID_Cliente</th>\n",
       "      <th>Cidade</th>\n",
       "      <th>Estado</th>\n",
       "      <th>Faturamento</th>\n",
       "      <th>Status_Entrega</th>\n",
       "      <th>Mes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>2026-01-01 03:00:00</td>\n",
       "      <td>Hollow Knight</td>\n",
       "      <td>Indie</td>\n",
       "      <td>7500.00</td>\n",
       "      <td>4</td>\n",
       "      <td>109</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>30000.00</td>\n",
       "      <td>Rápida</td>\n",
       "      <td>2026-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>2026-01-01 06:00:00</td>\n",
       "      <td>God of War</td>\n",
       "      <td>Ação</td>\n",
       "      <td>4500.00</td>\n",
       "      <td>5</td>\n",
       "      <td>148</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>BA</td>\n",
       "      <td>22500.00</td>\n",
       "      <td>Normal</td>\n",
       "      <td>2026-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>2026-01-01 08:00:00</td>\n",
       "      <td>Minecraft</td>\n",
       "      <td>Indie</td>\n",
       "      <td>549.61</td>\n",
       "      <td>2</td>\n",
       "      <td>141</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>1099.22</td>\n",
       "      <td>Normal</td>\n",
       "      <td>2026-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>2026-01-01 09:00:00</td>\n",
       "      <td>Resident Evil</td>\n",
       "      <td>Apocaliptico</td>\n",
       "      <td>1200.00</td>\n",
       "      <td>4</td>\n",
       "      <td>121</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>RJ</td>\n",
       "      <td>4800.00</td>\n",
       "      <td>Rápida</td>\n",
       "      <td>2026-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>2026-01-01 16:00:00</td>\n",
       "      <td>Overcooked</td>\n",
       "      <td>Indie</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>1</td>\n",
       "      <td>110</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>PR</td>\n",
       "      <td>2546.30</td>\n",
       "      <td>Normal</td>\n",
       "      <td>2026-01</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID_Pedido         Data_Pedido   Nome_Produto     Categoria  Preco_Unitario  \\\n",
       "0       1000 2026-01-01 03:00:00  Hollow Knight         Indie         7500.00   \n",
       "1       1001 2026-01-01 06:00:00     God of War          Ação         4500.00   \n",
       "2       1002 2026-01-01 08:00:00      Minecraft         Indie          549.61   \n",
       "3       1003 2026-01-01 09:00:00  Resident Evil  Apocaliptico         1200.00   \n",
       "4       1004 2026-01-01 16:00:00     Overcooked         Indie         2546.30   \n",
       "\n",
       "   Quantidade  ID_Cliente          Cidade Estado  Faturamento Status_Entrega  \\\n",
       "0           4         109  Rio de Janeiro     RJ     30000.00         Rápida   \n",
       "1           5         148        Salvador     BA     22500.00         Normal   \n",
       "2           2         141        Curitiba     PR      1099.22         Normal   \n",
       "3           4         121  Rio de Janeiro     RJ      4800.00         Rápida   \n",
       "4           1         110        Curitiba     PR      2546.30         Normal   \n",
       "\n",
       "       Mes  \n",
       "0  2026-01  \n",
       "1  2026-01  \n",
       "2  2026-01  \n",
       "3  2026-01  \n",
       "4  2026-01  "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vendas.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d416e866-ed46-4e48-8355-476701c9fbb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1e345b89-05e0-4ec0-8065-6d0c9be87ff7",
   "metadata": {},
   "outputs": [],
   "source": [
    "faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "69fcb6df-33da-4b26-8adc-c51b6ecf1491",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Mes\n",
       "2026-01    R$ 1,424,667.68\n",
       "2026-02    R$ 1,276,786.37\n",
       "2026-03    R$ 1,264,669.67\n",
       "2026-04    R$ 1,216,991.20\n",
       "2026-05      R$ 845,163.74\n",
       "Name: Faturamento, dtype: object"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "faturamento_mensal.map('R$ {:,.2f}'.format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5e59fda3-10cd-41da-9270-fc7e9b487ef6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABKUAAAJOCAYAAABm7rQwAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAuCZJREFUeJzs3Qd0VFXbBeCdnhASSOgQQiiKIEhQEAuIKF0QKYo0e0dELJ+9fJ+9UkTFhiK9CAhIVUEUBUGJogJSQkhCDQTS+/zrPf4ThxAgCUnu3Hn3w5qVycxk5tyz7x0yb84518vhcDhARERERERERERUibwr88WIiIiIiIiIiIgEi1JERERERERERFTpWJQiIiIiIiIiIqJKx6IUERERERERERFVOhaliIiIiIiIiIio0rEoRURERERERERElY5FKSIiIiIiIiIiqnQsShERERERERERUaVjUYqIiIjIYg6Hw+omeAT2IxERkb2wKEVERFTEhg0b0Lx58xJf5PGV2a4hQ4agMu3Zswc33HADWrdujauuugr3338/nn76abRs2RKffPIJrPDOO++Yvhg7dmyFPn9F55+SkoIXX3wRCxcuLNf2a3Pw4EE88sgjWL9+fYU8f0JCwgmZb9u27bSPz8nJQbt27Qofn5eXB0/x+OOPm22aO3eu1U0hIiIP4Gt1A4iIiNxVlSpVcPXVV5/xcTVr1oQnGzduHGJjY9GlSxccPnwYmzZtQnp6Oi655BJcf/318GQNGzZEdHR0heX/yiuvYP78+aYwRWX36KOPmuLggAEDKuX1li9fjvPOO++U969duxapqamV0hYiIiI7Y1GKiIjoFMLCwvDmm29COylKaSWjXV599dUKe35ON7NXP0qhOjs72xSlHnzwwVM+bunSpfDz80Nubm6ltIuIiMiuOH2PiIiIiKgEQkJC0KFDBzNycPv27cU+JjMzE6tXr0anTp0qvX1ERER2w6IUERFRORk9evRp11r5+OOPzf2vvfbaCbd/+eWXGDp0KC688EJccMEF6Nu3L95//33z4fZs15mSNaDkflkTp+iaN5999pmZ7tS2bVtceumluOmmm8y0o+LW65E2S7vksa1atcKVV16Jxx57DLt37y72dX/99VeMHDnSTPGTx8vUv+eeew779+9HaRw6dAj/+9//zM9L30h7V6xYcdqfWbNmDW6//XZc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",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (12, 6))\n",
    "faturamento_mensal.plot(kind = 'line', marker = 'o', linestyle = '-', color = 'green')\n",
    "plt.title('Evolução do Faturamento Mensal', fontsize = 16)\n",
    "plt.xlabel('Mês', fontsize = 12)\n",
    "plt.ylabel('Faturamento (R$)', fontsize = 12)\n",
    "plt.xticks(rotation = 45)\n",
    "plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2f5ca01d-e482-4f68-864c-2eee1e827e11",
   "metadata": {},
   "outputs": [],
   "source": [
    "vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending =  False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7e862572-26b7-4429-8684-3fcb4e135258",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Estado\n",
       "SP    R$991,586.05\n",
       "RJ    R$969,605.27\n",
       "BA    R$949,884.50\n",
       "CE    R$847,482.54\n",
       "RS    R$845,568.87\n",
       "PR    R$760,151.11\n",
       "MG    R$664,000.32\n",
       "Name: Faturamento, dtype: object"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas_estado.map('R${:,.2f}'.format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "04f2e641-0943-45f1-bc8b-cd424f84edb6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABKUAAAKyCAYAAAAEvm1SAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAATu5JREFUeJzt3QeYXGX5N+AnJARCSAgIJH86hhoSICQQG9KrdCkigoCClNBB2l9FSkBAkRYFEbBQVBQFpChKUzoEQUogdKRIgBDSCEn2u57zfbPfbrKBzezkzJb7vq65snPm7Mw7Z97szv7meZ/TraGhoSEAAAAAoEQLlPlgAAAAAJCEUgAAAACUTigFAAAAQOmEUgAAAACUTigFAAAAQOmEUgAAAACUTigFAAAAQOmEUgAAAACUTigFAFSloaGh3kPoFBzH+c8xBoD2qUe9BwAA1MZrr70Wm222Wav23XnnneOss86q+rH+/Oc/x+233x7nnXde1ffR1c2cOTOuvfbaePHFF+N///d/oyt54IEHYp999mn1/r/85S9jxIgR7XaunnDCCXH99dfH6aefHrvtttt8exwA6GyEUgDQCW2//fYfe/vQoUOrvu+HHnoojj766FhvvfWqvg8ibrzxxjj11FM/8bXqzBZZZJFWBalLLrlkVfdvrgJA+yaUAoBO6Nxzz51v9z1r1qz5dt9dieMYsfjii5urANCF6SkFAAAAQOmEUgBA/Pvf/47jjjsuNt100xgyZEisu+66sc0228Q555wTEydObNY7p9IL6NFHH43VV1899t577+L6H/7wh+L6scce2+Jj5G15aSofb/jw4fHss8/GLrvsEoMHD45NNtmkuO80bdq0uOKKK+IrX/lKbLDBBrHWWmvFZz7zmTjggAPiH//4R4uPkfczYcKEOOWUU+ILX/hCrL322sUSuT/+8Y/FPm+++WYcc8wxRY+i9ddfP/bdd994+umnWxzz448/Hocffnh89rOfLcaWS83OPPPMePfdd1t87B133DE++OCDOOOMM2LjjTcuvmeLLbaIH//4xzF16tTGffOYnXjiiY3L+PJ789g2deedd8Y3vvGN4nnna7LVVlsVr0c+t9bK45tLNfOxR40aVRyPfG132mmn+M1vfjPXBuB/+tOf4qtf/Wqx7K1y/H7yk580ew6VPmY59kMOOSRuueWW4rWr7D958uSYX/K1/NrXvhaf+9znisfLY5xLIfO1bc1cTTNmzIjf/e538fWvf72YCzm38ljnPjfddFOLj/vSSy/Ft7/97cbjuNdeexX9sT5Oa48lAHRFlu8BQBeXYUKGNBlQ5B/aGaS888478dhjj8Vll10W999/f/HH+wILLFAEHG+99Vbce++9scQSS8TnP//5GDhwYJse/6OPPooDDzwwunfvHhtttFEREK2xxhrx4YcfFgFBBkNLL7108Ud9t27dYuzYsXH33XfHPffcExdddFFsvvnmze5v0qRJsccee8Tbb79dhA0ZIOVzOf7444uA7dJLLy32GzZsWDz//PNx3333FaHBzTffHP/zP//TeD/ZuPrkk08uloANGjSoCLBybFdeeWX89a9/LZpvL7fccs0eO4OGvK9XXnmlOFarrrpqcf8ZQjzzzDPx05/+tNgvw5R83mPGjCnuI/dt2ucrl7T97Gc/K45JjjOXuVVej3y9fvGLX8Tyyy/fquOb4z/44IOL8CSfQ/ZxyjF997vfLcKaH/zgB832zXAyQ5mePXsWIU2vXr2K3kwZrN12221FSJjjaSpDxQwj11xzzVhllVWKudS7d++YH/K4Z+iXzyOPTY7vySefjKuuuir+8pe/FCHQpz71qY+dqzm+ww47LP7+979Hv379irBooYUWinHjxsWDDz5YXHLeNG3GnsHt/vvvH++//36sttpqxXysbJt9HrTlWAJAl9IAAHQKr776asNqq61WXFrrww8/bBgxYkTDWmut1fDoo482u23cuHEN6623XnF/Dz/8cOP2+++/v9j2la98pdn+v//974vtxxxzTIuP1dLYNtlkk2Lbzjvv3DBt2rRi28yZM4t/L7/88uK2Qw89tOGjjz5q/J4ZM2Y0nHLKKcVt++67b4uPse222zaMHz++cftpp53WeNv+++/fMHny5GJ73u9ee+1VbL/kkkuaPfc8Juuuu27Dvffe27g9x/ajH/2oxedfuf9tttmm4ZVXXmnc/sQTTxT3lbeNHTv2E4/X3/72t2L7Bhts0PD44483e61OPvnkxuM1a9asFo9zS8d3nXXWKV63ipdeeqnhi1/8YnHbLbfc0rj9F7/4RbFts802a3j55Zcbt3/wwQcNBx54YHHbyJEjW5xz+Zo0PU4fpzKHcnzzIo9BPpc8Nm+99Vbj9nwdc1x5nxdffPEc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EfPWXwwAAAAon1CqncpA6vUJH9R7GAAAAABdt6cUAAAAAJ2LUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAroUHr16lXvIQAAAFADPWpxJ0DnMauhIRbo1i3ao+7du8egQYOiPWvPxw8AAKA9EUoBzWSg8udHH493Jk2q91A6nE8tumh8ab216z0MAACADkEoBcwhA6n/vv9BvYcBAABAJ6anFAAAAAClE0oBAAAAUDqhFAAAAAClE0oBAAAAUDqhFAAAAAClE0oBAAAAUDqhFAAAAAClE0oBQCv16tWr3kMAAIBOo0e9BwAAFbMaGmKBbt2iPerevXsMGjQo2rP2fPwAAGB2QikA2o0MVO7+92MxYfKkeg+lw+nXe9H44uB16z0MAABoNaEUAO1KBlLvfjCx3sMAAADmMz2lAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAAAACidUAoAAACA0gmlAAA6gF69etV7CAAANdWjtncHANAxNTQ0RLdu3aI96t69ewwaNCjas/Z8/GgbgSgA84tQCgAgoghUxjz7aHwwZVK9h9Lh9Flk0Ri62nr1HkaH1Z4DPYEoAPOTUAoA4P/JQGri5PfrPQy6mAxUnnvxkZg69YN6D6XD6dWrT6y68rB6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99xz44477oj+/fvH4MGDY911141evXrFxIkT44033ohf/OIXccEFF8Rmm20WRx55ZKyyyirzb/QAAAAAdO5Q6uc//3lceumlse2228bVV18dQ4cOneu+//rXv+Laa6+NPffcMw488MA44IADajVeAAAAALpSKPX000/HDTfcUFRIfZJ11lmnuBx22GHxwx/+sK1jBAAAAKCrhlK5bG9eZY8poRQAAAAA8+Xse+PHj4+nnnoqpkyZUou7AwAAAKCTa3UoNWbMmNh3333jvvvua9w2adKkOPzww2PDDTeML3/5y7HBBhvEOeecEzNnzpxf4wUAAACgqyzfy35Se++9dyy77LKx4IILNm4/44wz4m9/+1txlr011lgjHnnkkbj88sujR48ecdRRR83PcQMAAADQ2UOpX//610XolGfUy8ApTZs2Lf785z8XYdW3vvWtYttGG20UCy20UFxzzTVCKQAAAACqD6Wuv/76+Mtf/hJ9+/aN/fffv3H71KlTY/r06cVyvn322adx+8SJE+Odd94ptu2yyy6x0047fdJDAAAAANDFfGIotfnmm8dNN90U/fr1i6OPPrpx+3nnnRdvvPFGjB49utn+t912W1x44YUxatSoWGyxxebPqAEAAADo3I3O+/TpUwRTGTbdc8898eGHH8a9995bXM/m5tlnqnJ55ZVXip5Sn/3sZ2O55ZYrvhcAAAAAquoptfvuuxfL9E455ZTo1q1bNDQ0xNChQ+Pggw9u3OerX/1qcYa+AQMGxIknntiauwUAAACgi2pVKNW9e/e44IIL4qmnnooXXnihCJ6GDRtWBFQVu+22W+ywww6x3XbbxaKLLjo/xwwAAABAVwilKgYNGlRcWrLzzjs3fv3000/HmmuuOU8Dyebo3/nOd+LBBx8sQrAMuI4//vjGs/01lfucc845MW7cuKIBe1ZpVc4ACAAAAEAn6CnV1LvvvhvXXHNNcXnrrbfmuP3999+P733ve7HrrrvO80COPPLIWGSRRYq+Vdddd12xXPDKK6+cY7/nn38+DjzwwCKIevTRR+OSSy4p+ljdeuut8/yYAAAAALTzSqknn3wy9t9//yJ4qpx975e//GWsscYaxfXf/e538cMf/jAmTJgQa6+99jwN4uWXXy6qn+6+++7o1atXLL/88nHIIYcU1VDf/OY3m+179dVXx2abbdZYmZWP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7Rg1alQ8+OCDsdZaa8Xaa69d21ECAAAA0KlUdfa9d999N7785S/HGWecES+//HI8/vjjMW3atLjrrrti7733jjFjxtR+pAAAAAB07VDq7LPPjsmTJ8fNN98c119/fTQ0NBTbzz///BgyZEhccMEFtR4nAAAAAF09lLrjjjviiCOOiBVXXLHZ2fcWWmih2H///ePJJ5+s5RgBAAAA6GSqCqU+/PDD6NevX4u3de/ePT766KO2jgsAAACATqyqUCqX6F199dUt3nbjjTfG4MGD2zouAAAAADqxqs6+l0v39t1339hxxx1jo402Kpbw3XTTTXHhhRfGP/7xj7jssstqP1IAAAAAunal1PDhw+OKK66IXr16FQFUNjq/8sor4+23345LLrkkPvOZz9R+pAAAAAB07UqptP7668e1114b06ZNi/fffz8WXXTR6N27d21HBwAAAECnVHUolSZNmhQTJ04svs5gKi8VyyyzTNtHBwAAAECnVFUo9cwzz8Rxxx0X48aNm+s+Tz/9dFvGBQAAAEAnVlUo9d3vfjfee++9+Pa3vx39+vWr/agAAAAA6NSqCqWeffbZOOuss2Lrrbeu/YgAAAAA6PSqOvve8ssvH7Nmzar9aAAAAADoEqoKpY4++ug4//zz48EHH4wPP/yw9qMCAAAAoFOravneyiuvHA0NDfH1r3+9xdu7desWTz31VFvHBgAAAEAnVVUodeKJJxaNznffffdYaqmlaj8qAAAAADq1qkKprII688wzY9ttt639iAAAAADo9KrqKbX00ktHr169aj8aAAAAALqEqkKpAw88MH784x/HSy+9VPsRAQAAANDpVbV877bbbov//Oc/sc0220Tfvn1j0UUXnaPR+e23316rMQIAAADQyVQVSmVz8y222KL2owEAAACgS6gqlMom5wAAAABQaihVMX78+Pjoo4+ioaGhuD5r1qyYOnVqPPzww7Hnnnu25a4BAAAA6MSqCqWeeeaZOProo+PFF19s8fbsKSWUAgAAAKCmodTZZ58dEydOjOOPPz7uuOOO6NmzZ2yyySZx9913F5df/vKX1dwtAAAAAF3EAtV807/+9a844ogjYt99940vfelLMWXKlPjqV78aP/3pT2PzzTePX/3qV7UfKQAAAABdO5SaPn16rLzyysXXn/70p2Ps2LGNt+2yyy7x2GOP1W6EAAAAAHQ6VYVSyyyzTLz66qvF1yuuuGJMmjQpXnvtteJ6LuV7//33aztKAAAAADqVqkKpLbfcMs4999y49dZbY6mlliqqpc4777yiYuryyy+P5ZdfvvYjBQAAAKBrh1IjR46MYcOGxe9///vi+oknnhi333577LTTTnH//ffHYYcdVutxAgAAANDVz743bdq0uOCCC+Kjjz4qrm+44YZx0003xb///e9Ya621YoUVVqj1OAEAAADo6pVSu+22W9x8882x4IILNm7LJXvbbLONQAoAAACA+RNKZSPzxRdfvJpvBQAAAIDqQql99tknzj777KJ/1Lvvvlv7UQEAAADQqVXVU+pPf/pTvP7667Hffvu1eHu3bt3iqaeeauvYAAAAAOikqgqldthhh9qPBAAAAIAuo6pQauTIkbUfCQAAAABdRlWhVC7d+yTLLLNMNXcNAAAAQBdQVSi16aabFn2jPs7TTz9d7ZgAAAAA6OSqCqVGjRo1Ryg1ZcqUeOSRR4oz8uXtAAAAAFDTUGqXXXZpcftee+0VP/jBD+LGG2+MjTfeuJq7BgAAAKALWKDWd5hh1J133lnruwUAAACgE6l5KPXYY49Fjx5VFWABAAAA0EVUlR6deOKJc2ybNWtWvPHGG/Hwww/HrrvuWouxAQAAANBJVRVKPfDAA3Nsy8bniy66aBxwwAFx0EEH1WJsAAAAAHRSVYVSf//732s/EgAAAAC6jAWqXb736quvtnjbCy+8oFIKAAAAgNpUSr3++uuNX19//fWx+eabR/fu3efY7+6774577723tXcLAAAAQBfU6lDq1FNPjbvuuquxf9TIkSNb3K+hoSE+//nP126EAAAAAHTdUOr73/9+UQGVodNJJ50UBx98cKywwgrN9llggQWib9++MWLEiPkxVgAAAAC6WijVv3//2HnnnRsrpTbaaKNYYokl5ufYAAAAAOikqjr7XoZT06ZNi3/961/x0UcfFdVTadasWTF16tR4+OGH49hjj631WAEAAADoyqHU/fffH0cccURMnDixxdt79+4tlAIAAACgtqHUj3/84+jXr1+cfvrpccMNNxS9pHbZZZfizHvXXHNN/OxnP6vmbgEAAADoIqoKpcaOHRunnXZabLHFFjFp0qS4+uqrix5TecnlfD/5yU/i0ksvrf1oAQAAAOgUFqjmm7J31IABA4qvV1555Rg3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KIKsRx99NK655prYZJNNGvfJMCuX3WXPqKYmTJjQ7Ppiiy02xz4plwCmxRdfvEbPEgCgdYRSAAAlGDNmTHzuc5+Lxx9/PLp161b0jcqG46uttlq8+eabxT6z93T697//XfSbygbplX5TleqplBVSCy20ULEsL8OtSuPzSvPzptZff/1iDHkGwKayyXkuPcyeVgAAZbJ8DwCgBrIp+WOPPTbX23PZ3cILL1ycTe+www4rls1lb6mnn3469tlnn2Kfvn37Fv9mVVT2nMrm5T169Ihzzjkn9t9//+Ix/vCHP8Sdd95Z7Jdn8ktHH310fP3rX4+RI0fGHnvsES+99NIc/a3222+/IoDKf3O/rIzKaq3777+/WB6oyTkAULZuDU0/UgMAYJ6dcMIJRY+oj3PddddFnz59iubjjzzySNHDaaWVVoq99967CJJSnlUvA6OHHnqoqKq69NJL49Zbby3O0JdL+XIJ3rrrrluEWPl92TR9r732Kr43A64f/ehH8eyzzxa9o4477rjiTH9nnnlm7LLLLsU+WSWVj//Pf/6zaJKeywIPOOCA2GyzzUo4SgAAzQmlAAAAACidOm0AAAAASieUAgAAAKB0QikAAAAASieUAgAAAKB0QikAAAAASieUAgAAAKB0QikAAAAASieUAgAAAKB0QikAAAAASieUAgAAAKB0QikAAAAASieUAgAAACDK9n8AxgR3tjNc75cAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1200x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (12, 7))\n",
    "\n",
    "vendas_estado.plot(kind = 'bar', color = sns.color_palette(\"blend:#7AB,#EDA\",7))\n",
    "plt.title('Faturamento por Estado', fontsize = 16)\n",
    "plt.xlabel('Estado', fontsize = 12)\n",
    "plt.ylabel('Faturamento (R$)', fontsize = 12)\n",
    "plt.xticks(rotation = 0)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "1c8f6f2d-0c94-41cf-9d85-6497b815f59c",
   "metadata": {},
   "outputs": [],
   "source": [
    "faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9759ed33-d988-4ad9-b768-c105c04744bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Categoria\n",
       "Indie           R$ 3,704,878.66\n",
       "Ação            R$ 1,593,000.00\n",
       "Apocaliptico      R$ 730,400.00\n",
       "Name: Faturamento, dtype: object"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "faturamento_categoria.map('R$ {:,.2f}'.format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "885c2bb8-e337-4118-8185-e14e7c3b2318",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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QikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgrVvHnzmt4FAAAAagGhFJQzd968mt6Feq1JkyapY8eO+SvLl9cyAABQ2zWt6R2A2qRJ48bpouv/lN6a8kFN7wpU2XrrtEkXnrZ/Te8GAADAYgmlYCERSL06eVpN7wYAAADUa9r3AAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwtW5UOqVV17JFwAAAADqrqapjpg6dWq6+uqr07PPPpt/7tKlSzrnnHPSaqutVtO7BgAAAEBdq5TaY4890lZbbZW22267fNl2223T9ttvn4466qg0fvz4svVOPfXUNHfu3NSjR490/PHHpylTpqTzzz9/kdu9++6701577ZW3GV/vuuuuRa47b968svsu7UdcZs6cmZfH1/79+6fOnTunTp06pX79+qUvvvii7PaTJ09Oxx57bL7NLrvskgYPHly2bMSIEfkxlvfll1+mnj17pj333DO98cYbVX7uAAAAAOqqGg+lwkUXXZReeumlfBkzZkx64okn0iqrrJJ69+6dA6OPP/44X9+rV6/UqlWr1KZNmzRgwIAcEFXkb3/7W7rhhhvSL3/5y7zNgQMH5iqrf/3rXxWuP2nSpDRnzpz0wgsvlO1HXFZeeeW8/JJLLknvv/9+evzxx/O+xfexzRC3i4ApgrXnn38+DRkyJAdijz32WIX3FY+le/fuacaMGem+++5LG2ywQbU9jwAAAAB1Ra0IpRa2xhprpMMOOyy9++67OcSJcKhFixZp5MiRZetsttlmuTqpIlGZFMHUlltumb7++uv00UcfpUaNGqVVV121wvXHjRuXNt1009SsWbNvLJs1a1Z65JFHcqXW6quvngOxM888M1dAxbJRo0aladOm5eVx+44dO6ajjz46B1MLizArKsBiO3feeWfeFgAAAEBDVCtnSkV4E+12UX3UunXrfN3ll1+ezjvvvNS4cePcJte2bdu06667LnIbLVu2zK1xBxxw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Lknvv/9+evzxx/O+xfexzTBnzpwcMEWwFrcdMmRIDsQee+yxCu8rHkv37t3TjBkz0n333Zc22GCDanseAQAAAOqKWhFKLWyNNdZIhx12WHr33XdziLPyyiunFi1apJEjR5ats9lmm+XqpIpEZVIEU1tuuWX6+uuv00cffZQaNWqUVl111QrXj3DoyCOPTBtvvHFaccUV0xlnnJHee++9HDLNmjUrPfLIIzmkWn311XMgduaZZ+YKqFg2atSoNG3atLy8WbNmqWPHjrnSKoKphUWYFRVgsZ0IwWJbAAAAAA1RrZwpFeFNtNtF9VHr1q3zdZdffnk677zzUuPGjXObXNu2bdOuu+66yG20bNkyt8YdcMABue3vZz/7WQ6MKjJp0qTcFliywgorpPXXXz9NmDAhB0hRDbXJJpuULd9www1zC96bb76ZXnvttdShQ4ccSJVstNFGuWJq4fuItsPYzs0335yaNGmy1M9LPA6Wr6r8XqC2cswAKnuccLwAqB0cl6kvKvsablpb2vcidIqqpgiA2rVrl7p27ZpOOumksnX22WefPK8pAp1oyevTp08OnC6++OJFbnfddddNL7/8cg6XTjnllBxwnXjiid9YL+ZDNW/efIHrVlpppTxL6vPPP88/R7VWSWnduF1Ft42f47YlUe0VFVIxr+qFF17IAdWmm2661M/TuHHjlvo2VF783hYVXEJdNHHixFzRCbAk/sYAqF0cl2koakUodeGFF6aDDz44zZ49Ow0fPjwPCt99993z/KiFq5+ixa50OfTQQ3Nwtfbaa1e43ah4ClFxdcwxx+Q2vIpCqQgjovKpvPg5WgZLYVS8sYufS9+X9ieWL/ymr/y6IR7XZZddlvbdd9902mmn5YDsgQce+MbjW5J4HCp5gMqqSvgNNLxPMeONj78xAGoHx2Xq22u5ToRSJdECd8IJJ6RPPvkkBzf33ntvnh01duzY3F735JNPlq0bLXPhs88++8Z27rjjjjwY/frrr18gGFpttdUqvN8IuKINr0uXLvnnqNaK1rxotYv7iXArqpu22WabvPz1118va/H74IMP8rpR5dW06f89nbFubLNkzTXXzIFUiHAqwrTTTz893XbbbWW3qYw4KDkwAZXleAFUlr8xAGoXx2Uailo56DyqieIT/r59++aKpQh44h9knPEuwqUIgOLseu3bt8/znRa2ww475ADr0UcfzWfve/HFF3MF1hFHHFHh/R1yyCF5hlW0+X311Vfp2muvzcPWYztRRRWBUtz3hx9+mC/xfbQORotf586dc8VT3CZuG9uIIeYRPFUkKqgGDRqU2wqvuuqqan/uAAAAAOqCWhlKRQB1zTXXpKlTp+bgJoKhoUOH5mqmSy+9NM+fivDnlltuKWvRKy/OunfjjTfmNsAIln7xi1+kAQMGpP322y8vHz16dB6WHmfYCxEgde/ePfXq1SvttNNOafz48enWW28t23a0F0ZVVLdu3fJsq3XWWSddcMEFeVlUOg0bNiy9+uqraeedd87tgXH2vWhHXJQI0uJxRFAWZ/EDAAAAaGgazZ8/f36qQ0ohzuJCn8qIKqw4m1/p7H61vRcz2hFjULoSzuXvuDOHp1cnT6vp3YAq26TDmmnYwGNqejeAOsDfGAC1i+MyDe21XKtmSlXGsoZRYcqUKfkMf3UhkAIAAACoj2pl+97yFu13/fr1q+ndAAAAAGiwGmQoBQAAAEDNEkoBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFq3Oh1CuvvJIvAAAAANRdTVMdMXXq1HT11VenZ599Nv/cpUuXdM4556TVVlutpncNAAAAgLpWKbXHHnukrbbaKm233Xb5su2226btt98+HXXUUWn8+PFl65166qlp7ty5qUePHun4449PU6ZMSeeff/4it/v444+nAw88MG8r7mPQoEFp3rx5Fa4b15fuu7QfcZk5c2ZeHl/79++fOnfunDp16pT69euXvvjii7LbT548OR177LH5NrvssksaPHhw2bIRI0bk+y/vyy+/TD179kx77rlneuONN5bp+QMAAACoi2o8lAoXXXRReumll/JlzJgx6YknnkirrLJK6t27dw6MPv7443x9r169UqtWrVKbNm3SgAEDckBUkf/85z85ODrttNPS6NGj09ChQ3M4dMcdd1S4/qRJk9KcOXPSCy+8ULYfcVl55ZXz8ksuuSS9//77OeiKfYvvBw4cmJfF7SJgimDt+eefT0OGDEl33313euyxxyq8r3gs3bt3TzNmzEj33Xdf2mCDDarteQQAAACoK2pFKLWwNdZYIx122GHp3XffzSFOhEMtWrRII0eOLFtns802y9VJFYnbHX744bnFr3HjxmnDDTdMXbt2TaNGjapw/XHjxqVNN900NWvW7BvLZs2alR555JFcqbX66qvnQOzMM8/MIVcsi21OmzYtL4/bd+zYMR199NE5mFpYhFlRARbbufPOO/O2AAAAABqiWjlTKsKbu+66K1cftW7dOl93+eWXp/POOy+HTNEm17Zt27TrrrtWePu99947X8q3yz311FOpW7duiwylvvrqq3TIIYfkQCtCrDPOOCO3/r311lu5GmqTTTYpWz+WxzbffPPN9Nprr6UOHTosEGhttNFGuWJq4WqsaDuM7dx8882pSZMmS/28RPsiy1dVfi9QWzlmAJU9TjheANQOjsvUF5V9DTetLe17ETp9/fXXOQBq165drmw66aSTytbZZ5998rymCHSita5Pnz7pgAMOSBdffPFit/3555/ndVdaaaXcNleRWLb11lvn9WJwelQ5RYD08MMP59uHUitfaN68ef4ac6XiUvq5/PLSPKoQ1V5RIRUzq6JFMAKqqMxaWhGesfzE7y0q3aC+mDhxYq7oBFgSf2MA1C6OyzQUtSKUuvDCC9PBBx+cZs+enYYPH54Hhe++++55flR5LVu2TBtvvHHZ5dBDD83B1dprr13hdmOIeLTVRZtcbDduX5E4i195EUhFe97TTz+dq6VCvLGLFsLS96X9ibBq4Td95dcN8bguu+yytO++++Y5V6ecckp64IEHvvH4liQqx1TyAJVVlfAbaHifYsYbH39jANQOjsvUt9dynQilSqIF7oQTTkiffPJJDm7uvffePDtq7Nix+ax7Tz75ZNm60TIXPvvsswq3FYFS3759009+8pPcite06aIf6nXXXZfb/cpXyUSQtOKKK+b7WWGFFXJ10zbbbJOXvf766/m69ddfP33wwQe5jS+qvEr3EetGaFay5ppr5kAqRDgVYdrpp5+ebrvttsXu18LioOTABFSW4wVQWf7GAKhdHJdpKGrloPOoJopP+CNUitlNEfDEP8g4412ERREA3XDDDal9+/Z5vtPCSmfq69+/fzr77LOXGPy8+uqrOSyaPn163v6gQYNy2160EEZLVwRKcd8ffvhhvsT30ToYbX+dO3fOFU/XXnttnks1YcKEPMQ8gqeKRAVVbP/ll19OV111VbU9ZwAAAAB1Sa0MpSKAuuaaa9LUqVNzcBPB0NChQ/NQ8UsvvTTPn4rw55ZbbskVSwuL9r8IriJoiqHopUtUYYXRo0fnn99777388xVXXJEDrgMPPDCHTDH36fbbb89nySu1F0ZVVAxKj9lW66yzTrrgggvysgi8hg0bloOtnXfeOZ144on57HvRjrgoEaTF44iWwmgTBAAAAGhoGs2fP39+qkNKIc7iQp/KiCqsOJtf6ex+tb0XM6q/YlC6Es7l77gzh6dXJ0+r6d2AKtukw5pp2MBjano3gDrA3xgAtYvjMg3ttVyrZkpVxrKGUWHKlCn5DH91IZACAAAAqI9qZfve8hbtd/369avp3QAAAABosBpkKAUAAABAzRJKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFA4oRQAAAAAhRNKAQAAAFC4plW94eTJk9NNN92Unn/++fTpp5+mVq1apR122CH16tUrbbjhhtW7lwAAAADUK1UKpSZNmpQOP/zw1LRp09SlS5e0xhprpOnTp6eRI0emp556Kt1///2CKQAAAACqN5QaOHBgWmedddKdd96ZVllllbLrP/vss3Tsscem6667Lg0aNKgqmwYAAACgAajSTKlRo0alnj17LhBIhfj5xBNPzMsBAAAAoFpDqWjba9asWYXL4vrZs2dXZbMAAAAANBBVCqW22mqrdPfdd6f58+cvcH38fNddd6Utt9yyuvYPAAAAgHqoSjOl+vTpk4444oh0wAEHpH333Te1bds2Dzp/7LHH0ltvvZVuv/326t9TAAAAABp2KBWVUrfddlu69tpr080335wrpBo1apQrpIYOHZp23HHH6t9TAAAAABp2KBV22mmndP/996dZs2alTz/9NK266qqpefPmedn//ve/1K5du+rcTwAAAAAa+kypzTffPI0dOzZ/H0HUWmutVRZIjR49Orf0AQAAAMAyV0oNGzYszZw5M38f7XpRJfXMM898Y72XXnppkWfmAwAAAIClCqVmz56dBg0alL+P+VERSi2scePGaZVVVkknn3yyZxcAAACAZQ+levbsmS9hs802S/fdd1/aeuutK3tzAAAAAFi2QecTJkyoys0AAAAAYNnOvvfss8+mkSNH5rPvzZs3b4Fl0d53+eWXV3XTAAAAANRzVQqlbrvttjRw4MC04oorptatW+cQqryFfwYAAACAZQ6l7r777tStW7d02WWXOdMeAAAAAEut8dLfJKUPPvggHXrooQIpAAAAAIoLpTp27Jhee+21qt0jAAAAAA1eldr3zj333HTaaaellVdeOW2zzTapefPm31jn29/+dnXsHwAAAAD1UJVCqSOOOCKfcS/CqUUNNX/llVeWdd8AAAAAqKeqFEpdeuml1b8nAAAAADQYVQqlDjrooOrfEwAAAAAajCqFUmH27NnpgQceSM8991yaPn16uvzyy9MLL7yQtthii7T11ltX714CAAAAUK9U6ex7H374YTrkkEPSZZddlt566600duzY9OWXX6ann346HX300emll16q/j0FAAAAoGGHUldffXX64osv0qOPPpoeeuihNH/+/Hz9DTfckLbaaqt04403Vvd+AgAAANDQQ6mRI0emPn36pPXWW2+Bs++tuOKK6bjjjkv//e9/q3MfAQAAAKhnqhRKffXVV2n11VevcFmTJk3SnDlzlnW/AAAAAKjHqhRKRYvePffcU+GyRx55JG255ZbLul8AAAAA1GNVOvtetO517949HXjggWn33XfPLXx//OMf00033ZT+8Y9/pNtuuy0tL6+88kr+uvnmmy+3+wAAAACgFlZK7bDDDun2229PzZs3zwFUDDq/44470vTp09Ott96adtppp2rf0alTp6Yzzjgj/exnP8uX/v37p08++aTa7wcAAACAWhpKhR133DH99re/Tf/+97/T008/nUaPHp0efPDBtPPOOy/VdvbYY4/cDrjddtvly7bbbpu23377dNRRR6Xx48eXrXfqqaemuXPnph49eqTjjz8+TZkyJZ1//vmL3O7jjz+eK7liW3EfgwYNSvPmzVvk+kOHDk277bZbvv+jjz46vfHGG2XLZs6cmUOwzp07p06dOqV+/frlsw+WTJ48OR177LF5/3fZZZc0ePDgsmUjRozI91/el19+mXr27Jn23HPPBe4HAAAAoKGocigVPv/88/Thhx/msCiqlt57772yy9K46KKL0ksvvZQvY8aMSU888URaZZVVUu/evXOQ9PHHH+fre/XqlVq1apXatGmTBgwYkAOiivznP//JwdFpp52Ww7IInCIcimquijz00EPpzjvvTL/+9a/T888/n7bYYoscgkUFWLjkkkvS+++/n4Ou2Lf4fuDAgXlZDHWPgCmCtbjtkCFD0t13350ee+yxCu8rHku0Ps6YMSPdd999aYMNNliq5woAAACgwYZSEyZMSN26dcvVUlHtU9FlWayxxhrpsMMOS++++24OcVZeeeXUokWLNHLkyLJ1Nttss1ydVJG43eGHH566dOmSGjdunDbccMPUtWvXNGrUqArXj3DoyCOPTBtvvHFaccUVc5tgBGsRMs2aNSsPb4+QKs44GIHYmWeemUOuWBbbnDZtWl7erFmz1LFjx1xpFcHUwiLMigqw2E6EYLEtAAAAgIaoSoPOL7jggvTRRx/laqQIWKpbhDd33XVXrj5q3bp1vu7yyy9P5513Xg6Zok2ubdu2adddd63w9nvvvXe+lG+Xe+qpp3KQVpFJkybltsCSFVZYIa2//vo5fIvHF9VQm2yySdnyCLlim2+++WZ67bXXUocOHXIgVbLRRhvliqmF7yPaDmM7N998c2rSpMlSPy9RkcbyVZXfC9RWjhlAZY8TjhcAtYPjMvVFZV/DVQqlXn311XTllVemffbZJ1WHaN+L0Onrr7/OAVC7du1yZdNJJ51Utk7cV8xrikAn2vziDIAHHHBAuvjii5fYYhjrrrTSSrltriIxHyqGtpcX68csqbh9iGqtktK6cbuKbhs/x21LotorKqRiXtULL7yQA6pNN900La1x48Yt9W2ovPi9RaUb1BcTJ07MFZ0AS+JvDIDaxXGZhqJKodS666672KHhS+vCCy9MBx98cJo9e3YaPnx4HhS+++675/lR5bVs2TK32JUuhx56aA6u1l577Qq3G0PEo60u2uRiu3H7RYURUflUXvwcLYOlMCre2MXPpe9L+xPLF37TV37dEI/rsssuS/vuu2+ec3XKKaekBx544BuPb0mickwlD1BZVQm/gYb3KWa88fE3BkDt4LhMfXstL5dQqm/fvrlSKmY/bbPNNnkOU3WIFrgTTjghD02P4Obee+/Ns6PGjh2b2+uefPLJsnWjZS589tlnFW4rzggY+/mTn/wkz4hq2nTRDzUCrmjDixlUIaq1ojUvWu3ifqKdL6qb4rGG119/vazF74MPPsjrRpVX6T5i3dhmyZprrpkDqRDhVIRpp59+errtttsWu18Li4OSAxNQWY4XQGX5GwOgdnFcpqGo0qDzCGrizHQxaDxa0jbffPMFLsvaAhXVRPEJf4RKUbEUAU/8g4wz3kXVUQRAN9xwQ2rfvn2e77Sw0pn6+vfvn84+++wlBj+HHHJInmEVM6S++uqrdO211+bAbYcddshVVBEoxX3HmQbjEt9H62C0+HXu3DlXPMVt4raxjRhiHsFTRaKCatCgQenll19OV1111TI9TwAAAAB1VZUqpSLsiUHnUYUUA8erWwRQ11xzTfrRj36Ug5to7xs6dGiuMnrwwQdzyBTljLfcckuuWFpYtP9FcBXrx6WkU6dOuTpp9OjRufLqT3/6U/r2t7+dA6SouIogK0Kn2Patt95atu24/9iPGJQeVVRxdsHzzz8/L4t9GTZsWJ5ttfPOO+d2vjj7XrQjLkoEaZdeemkO3SLEW9y6AAAAAPVRo/lR8rSUoo3tiiuuSPvtt18q2ogRI/LXZQ1yIhCKs/mVzu5X23sxo/orqtKUcC5/x505PL06eVpN7wZU2SYd1kzDBh5T07sB1AH+xgCoXRyXaWiv5SpVSsWMpIXPOFeU6qgqmjJlSj7DX10IpAAAAADqoyrNlDrxxBPT9ddfnwd810XrrLNO6tevX03vBgAAAECDVaVKqccffzy9++67eQD4qquumlq2bLnA8kaNGi1wpjwAAAAAWOZQKoabd+3atSo3BQAAAICqhVIx5BwAAAAACg2lSmbMmJHmzJmTSifwmzdvXpo1a1YaPXp0OuKII5Zl0wAAAADUY1UKpSZMmJD69u2bJk+eXOHymCkllAIAAACgWkOpq6++On366afp7LPPTiNHjkzNmjVLXbp0Sc8880y+DB8+vCqbBQAAAKCBaFyVG7388supT58+qXv37mn//fdPM2fOTEceeWQaPHhw+sEPfpDuvPPO6t9TAAAAABp2KDV79uzUoUOH/P0GG2yQJk6cWLbs4IMPTmPGjKm+PQQAAACg3qlSKPXtb387vfPOO/n79dZbL33++edpypQp+edo5fvkk0+qdy8BAAAAqFeqFErttddeaeDAgenPf/5zatu2ba6Wuu6663LF1LBhw9K6665b/XsKAAAAQMMOpXr37p06deqUHnzwwfxz//7905NPPpl+9KMfpX/961/p5z//eXXvJwAAAAAN/ex7X375ZbrxxhvTnDlz8s+77rpr+uMf/5j+85//pC222CK1b9++uvcTAAAAgIZeKfXjH/84Pfroo2mFFVYouy5a9vbdd1+BFAAAAADLJ5SKQeatWrWqyk0BAAAAoGqh1DHHHJOuvvrqPD/qww8/rP69AgAAAKBeq9JMqT/84Q/pvffeSz/72c8qXN6oUaM0fvz4Zd03AAAAAOqpKoVSP/zhD6t/TwAAAABoMKoUSvXu3bv69wQAAACABqNKoVS07i3Jt7/97apsGgAAAIAGoEqh1B577JHnRi3OK6+8UtV9AgAAAKCeq1Iodfnll38jlJo5c2Z68cUX8xn5YjkAAAAAVGsodfDBB1d4/VFHHZWuuuqq9Mgjj6Tvf//7Vdk0AAAAAA1A4+reYIRRTz31VHVvFgAAAIB6pNpDqTFjxqSmTatUgAUAAABAA1Gl9Kh///7fuG7evHnp/fffT6NHj06HHnpodewbAAAAAPVUlUKp559//hvXxeDzli1bph49eqSePXtWx74BAAAAUE9VKZT629/+Vv17AgAAAECD0biq7XvvvPNOhcveeOMNlVIAAAAAVE+l1HvvvVf2/UMPPZR+8IMfpCZNmnxjvWeeeSY999xzld0sAAAAAA1QpUOpiy++OD399NNl86N69+5d4Xrz589PO++8c/XtIQAAAAANN5S66KKLcgVUhE7nnntuOvnkk1P79u0XWKdx48Zp1VVXTZ07d14e+woAAABAQwul1lprrXTQQQeVVUrtvvvuqXXr1stz3wAAAACop6p09r0Ip7788sv08ssvpzlz5uTqqTBv3rw0a9asNHr06HTmmWdW974CAAAA0JBDqX/961+pT58+6dNPP61weYsWLYRSAAAAAFRvKHX99den1VdfPV166aXp4YcfzrOkDj744HzmvXvvvTcNHTq0KpsFAAAAoIGoUig1ceLEdMkll6SuXbumzz//PN1zzz15xlRcop3vlltuSUOGDKn+vQUAAACgXmhclRvF7Kh27drl7zt06JAmTZpUtmzvvfdO48ePr749BAAAAKDeqVIo1b59+1wtFdZbb7083Pz111/PP3/99dfpiy++qN69BAAAAKBeqVIo1a1btzRw4MB05513platWqUtt9wyz5f629/+lm6++ea00UYbVf+eAgAAANCwZ0qdcMIJ6aOPPkpjx47NP1944YWpR48e6ZRTTkktW7bMM6UAAAAAYJlDqUceeSTtuuuu+ax7cba9s88+u2zZVlttlZ588sn0xhtvpA022CAHUwAAAACwzO17/fr1S2+//fYC1w0ePDjNmDEjfx9B1NZbby2QAgAAAKD6Qqn58+cv8PPcuXPTDTfckKZOnVrZTQAAAABA1QedLyqoAgAAAIDlHkoBAAAAQFUIpQAAAACoe6FUo0aNqmdPAAAAAGgwmi7Nyr169UrNmjVb4LqePXumFVZY4RtB1ZNPPlk9ewgAAABAww2lDjrooOW7JwAAAAA0GJUOpa644orluycAABSuefPmNb0LAEADZdA5AFBrzZ03r6Z3oV5r0qRJ6tixY/7K8uW1DADLOFMKAKBITRo3Tqc//qc06cMPa3pXoMo2at06Xbf3/jW9GwBQ6wilAIBaLQKp/06fVtO7AQBANdO+BwAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFK7OhVKvvPJKvgAAAABQd9WZs+9NnTo1XX311enZZ5/NP3fp0iWdc845abXVVqvpXQMAAACgrlVK7bHHHmmrrbZK2223Xb5su+22afvtt09HHXVUGj9+fNl6p556apo7d27q0aNHOv7449OUKVPS+eefv8Ttv/TSS3n7izNv3ryy+y7tR1xmzpyZl8fX/v37p86dO6dOnTqlfv36pS+++KLs9pMnT07H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q9Ozzz6bf+7SpUs655xz0mqrrVbTuwYAAABAXauU2mOPPdJWW22Vtttuu3zZdttt0/bbb5+OOuqoNH78+LL1Tj311DR37tzUo0ePdPzxx6cpU6ak888/f4nbf+mll/L2l2To0KFpt912y/d/9NFHpzfeeKNs2cyZM1P//v1T586dU6dOnVK/fv3SF198UbZ88uTJ6dhjj837v8suu6TBgweXLRsxYkR+jOV9+eWXqWfPnmnPPfdc4H4AAAAAGooaD6XCRRddlMOjuIwZMyY98cQTaZVVVkm9e/dO8+bNSx9//HG+vlevXqlVq1apTZs2acCAATkgWpT58+enBx54IB133HFp9uzZi73/hx56KN15553p17/+dXr++efTFltskUOw2Ea45JJL0vvvv58ef/zxvG/x/cCBA/OyOXPm5IApgq+47ZAhQ9Ldd9+dHnvssQrvKx5L9+7d04wZM9J9992XNthgg2V67gAAAADqoloRSi1sjTXWSIcddlh69913c4iz8sorpxYtWqSRI0eWrbPZZpvl6qRFOffcc9P999+fw6UliXDoyCOPTBtvvHFaccUV0xlnnJHee++9HDLNmjUrPfLII3k7q6++eg7EzjzzzFwBFctGjRqVpk2blpc3a9YsdezYMVdaRTC1sAizogIsthMhWGwLAAAAoCGqlTOlIry56667cvVR69at83WXX355Ou+881Ljxo1zm1zbtm3Trrvuusht9OnTJ7Vr1y4HS0syadKk3BZYssIKK6T1118/TZgwIQdIUQ21ySablC3fcMMNcwvem2++mV577bXUoUOHHEiVbLTRRrliauH7iLbD2M7NN9+cmjRpstTPCwAAAEB90bS2tO9F6PT111/nACjCpK5du6aTTjqpbJ199tknz2uKQCfa/CJ0OuCAA9LFF19c4TZjG5UV86GaN2++wHUrrbRSniX1+eef55+jWquktG7crqLbxs9x25Ko9ooKqZhX9cILL+SAatNNN01LK2ZqsXwJC6lPHDOoDxyXqU8cl4HKHiccL6jrKvsarhWh1IUXXpgOPvjgPPtp+PDheVD47rvvnudHldeyZcvcYle6HHrooTm4WnvttZfp/iNEisqn8uLnaBkshVHRqhc/l74v7U8sL/1cUn7dEI/rsssuS/vuu2867bTT0imnnJLnXS38+JZk3LhxVX6MVO51EO2XUF9MnDjxG8cnqEscl6lvHJeByvLej4aiVoRSJdECd8IJJ6RPPvkkBzf33ntvnh01duzY3F735JNPlq0bLXPhs88+W+b7jYAr2vC6dOmSf45qrWjNi1a7uJ9o54vqpm222SYvf/3118ta/D744IO8blR5NW36f09nrBvbLFlzzTVzIBUinIow7fTTT0+33XZb2W0qI9oZfWIMVFZVKjIBWH4cl4HKVJdEIOW9H/XltVynQqmSqCaKAeJ9+/bNA8Uj4Il/kHHGu8033zzPlbrhhhtS+/bt83ynZXXIIYekm266Ke222245hLruuuvysPUddtghh08RKMV9x32G+D5aB6PFr3Pnzrni6dprr837PXny5DzEPEKnikQF1aBBg3IwddVVV+WzCFZWPAcOTEBlOV4A1C6Oy0Blee9HQ1Erz74X//iuueaaNHXq1BzcRPn+0KFDczXTpZdemudPxRDyW265JYdGS2v06NF5WHqcYS9EQNS9e/fUq1evtNNOO6Xx48enW2+9tWzb0V4YVVHdunXLs63WWWeddMEFF+RlUek0bNiw9Oqrr6add945nXjiifnse9GOuCgRpMXjiFbFCN0AAAAAGppG8+fPn5/qkFKIs7jQpzKiCivO5lc6u19tL3sbM2ZMHpQuLV/+jjtzeHp18rSa3g2osk06rJmGDTympncDqk23e+9M/53uuEzdtUXbNdMjRxxd07sB1AHe+9HQXsu1sn1vcZY1jApTpkzJZ+erC4EUAAAAQH1UK9v3lrdov+vXr19N7wYAAABAg9UgQykAAAAAapZQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAACglmjevHlN7wIURigFAABApcybP6+md6Fea9KkSerYsWP+yvLltVw7NK3pHQAAAKBuaNyocRr8+pD03qz3a3pXoMq+3fxbqeeGJ9b0biCUAgAAYGlEIPXWzLdrejeAekD7HgAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFq9eh1CuvvJIvAAAAANQuTVM9NHXq1HT11VenZ599Nv/cpUuXdM4556TVVlutpncNAAAAgLpWKbXHHnukrbbaKm233Xb5su2226btt98+HXXUUWn8+PFl65166qlp7ty5qUePHun4449PU6ZMSeeff/4it3vhhRemLbfcsmy7cfnd735Xtvyhhx5KXbt2zfd38MEHp5deeqlsWdzPVVddlb73ve/l25188slp2rRpZcs33XTT9Pzzzy9wfw8++GB+HPfcc081PjsAAAAAdUedCqXCRRddlEOhuIwZMyY98cQTaZVVVkm9e/dO8+bNSx9//HG+vlevXqlVq1apTZs2acCAAalTp06L3Oa4cePSJZdcUrbduBx22GF5WQRKsezKK69Mo0aNSj/84Q9z8DRr1qy8/JZbbskVWRE0/f3vf08rrbRSOu+88xZ5X0OGDEmXXnppuvHGG9ORRx65HJ4hAAAAgNqvzoVSC1tjjTVygPTuu+/mQGrllVdOLVq0SCNHjixbZ7PNNkvHHntshbefPXt2evXVV3OlVEXuv//+tP/+++dQa4UVVkjdu3fPYdejjz5atjwqsr71rW+lli1b5gDsmWeeSe+8884C25k/f34Oo37zm9+k4cOH55ZCAAAAgIaqzs+Uev/999Ndd92V2+Fat26dr7v88stztVLjxo1zS13btm3TrrvuWuHtJ0yYkL7++utcufTiiy/mqqtDDjkknXDCCfn2kyZNyj+Xt9FGG+XbffbZZ+l///tf2mSTTRYIyWJ21cSJE9O6666br5szZ04644wz0l//+tf0xz/+sex6AAAAgIaqaV1s34vQKYKkCHvatWuX5z2ddNJJZevss88+aZdddkk333xzbsXr06dPOuCAA9LFF1/8je1FsPSd73wnHX300emXv/xlPltftP5FIBXB1BdffJGaN2++wG2iRW/mzJl5WYjqrIWXl5aFmGcVlVQrrrhiGjFiRN6fqoj5VSxfTZo0qeldgGrjmEF94LhMfeK4TH3guEx94rhc889tnQulYih5DBuPtrtogxs8eHDafffdc0tdedFKt/HGG5ddDj300Bxcrb322gust/POO+dLydZbb51b/aI9L0KpCKS+/PLLBW4TP8f9lcKq0nyp8sujhbBkm222yWcDfO655/I8qs033zzttddeS/3YY/YVy0/8Pjt27FjTuwHVJio2Fz4+QV3iuEx947hMXee4TH3juFzz6lwoVdKsWbMcGn3yySfplFNOSffee2+eHTV27Ng84+nJJ58sW7dDhw5lVVELi/VmzJiRDj/88LLrIvCKaqcQgdZrr722wG2ipW+33XbLbXprrbVW/rnUwjd9+vQ826p8S98RRxyR9/f73/9+OvHEE9PZZ5+d1ltvvXxmvqURLYo+mQAqa2mPMQAsX47LALWL4/LyrZSqTGFNnQ2lSk477bR8Vry+ffvm1rgIkSK4GThwYK5Iija8G264IbVv3z5tuOGG37h9DCC/4oorcki000475TP3RQVW//798/KosIp2vn333TcPO7/77rvTBx98kFsGQ1RtxRn4IjCK6qloLYx2wLi/ikTrXgRnsc0HHnggrb766pV+rPG4hFJAZTleANQujssAtYvjcs1rXB9eRNdcc02aOnVquuqqq3JJ6dChQ3N1U5ztLkKiGEoewVGcPW9hES5FAPWLX/wiD0U/66yz0s9//vN04IEH5uXf/e53c8tgLI+w6U9/+lPefilMinAp2gePOuqo/PWrr75K119//SL3N0Kya6+9Ns/EikBNDysAAADQEDWaH6VC9VRUTpWqmeqyCK6igmvbbbeV5BbguDOHp1cnT6vp3YAq26TDmmnYwGNqejeg2nS798703+mOy9RdW7RdMz1yxNE1vRtQbS74z0XprZlv1/RuQJWtt3L7dPGWF9b0btRrlc0x6nz73uLU9TAKAAAAoL6q8+17AAAAANQ9QikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQqnFeOWVV/IFAAAAgOrVtJq3Vy9MnTo1XX311enZZ5/NP3fp0iWdc845abXVVqvpXQMAAACoFxpUpdQee+yRttpqq7Tddtvly7bbbpu23377dNRRR6Xx48eXrXfqqaemuXPnph49eqTjjz8+TZkyJZ1//vmL3O7LL7+cfvzjH+dtxn3cf//9ZctuuummdPTRRy+w/ocffpjXP/jgg9P06dOX06MFAAAAqL0aVCgVLrroovTSSy/ly5gxY9ITTzyRVlllldS7d+80b9689PHHH+fre/XqlVq1apXatGmTBgwYkDp16lTh9j755JN04oknph/96Edp1KhR6bLLLktXXHFFGjt2bIXrv/vuu+nII4/M277rrrtS27Ztl/MjBgAAAKh9GlwotbA11lgjHXbYYTksikBq5ZVXTi1atEgjR44sW2ezzTZLxx57bIW3j1Br9dVXz9VWTZs2Td/97ndTt27d0t133/2NdSdOnJgOP/zw9J3vfCfdcsst+b4AAAAAGqIGP1Pq/fffzxVL0dbXunXrfN3ll1+ezjvvvNS4cePckhfVTLvuumuFt3/ttdfSJptsssB1G220UXrggQcWuC6qqE455ZS07777posvvnip9nH+/Pn56+zZs1OTJk2W8hGyNOL53XC9NdIKTRt8Xksd1n7t1rkFOS5QH47Lm7dpk1Zs7LhM3bVBq1aOy9Sr4/I6K62dms5v8G8lqcParbSW4/JyVnpuS3nGojSav6Q16pGY9/TBBx+kFVZYIX399ddpzpw5qV27dqlr167ppJNOyi11JZ9//nm6+eabc5vfq6++mg444IAKw6Ro7YvtxGD0kpgpNWTIkPSXv/wlz5S69957c6C0zTbb5GqpBx98MK211lqV3u+47bhx46rhGQAAAAAoRhQANWvWbJHLG1y8feGFF+YB4xH0DB8+PA0ePDjtvvvuCwRSoWXLlmnjjTcuuxx66KE5uFp77bUXWK958+bps88+W+C6L7/8MrcAlnz11Vf5fmKw+jHHHJPnV0V73+J+MeVFW2D8IqNyq1GjRsv0+AEAAACWp6h/irndkWcsToMLpUoiEDrhhBPyoPJoq4tqppgdFQPK46x7Tz75ZNm6HTp0yF8XDp9CtO49++yzC1w3adKkHGSVdOzYMe244475++uvvz4ddNBB6YILLkhXXnllpfY1wqjKBlgAAAAAdUGDH9Bw2mmnpU033TT17ds3VzhFmBR90gMHDszVVNHmd8MNN6T27dunDTfc8Bu3j9a/GTNmpDvuuCO38f3rX/9KjzzySDrkkEMqvL9o2/vlL3+ZHn744XwbAAAAgIaowYdSEUBdc801aerUqemqq67K7XhDhw7NA8wvvfTSPPR8woQJ+Wx5MYtqYdH2N2zYsPTnP/85de7cOQ9Ij8tOO+20yPuMZRGGxRyqf/7zn8v5EQIAAADUPg1q0PnSGjFiRP4aM6gAAAAAqD5CKQAAAAAK1+Db9wAAAAAonlAKAAAAgMIJpQAAAAAonFAKAAAAgMIJpQAAAKAgzjUG/49QCqh2/qMFqFnz5s2r6V0A4P83d+7c/PXLL7/Mx+fPP/+8pncJao2mNb0DQN3/T7ZJkyYLXNeoUaOycKr0PQDFHpfff//99NJLL6Wvvvoqrb322uk73/lOTe8aQIM9Jr/22mvp+uuvT1988UX68MMPU8+ePdO+++7rb2UaPKEUsMz/ycYnPldccUX+9Cf+oz3mmGPSxhtvnFq0aFHTuwjQoMSHAXFcnjBhQjr55JPTZpttlmbMmJEmTpyYf44LAMWJY/Ibb7yR/z7u0aNH+ta3vpV/7tu3b5o2bVrq3r27D3Jp0IRSwDK98YlA6tBDD01rrbVW2m+//dJf/vKX1Lt37/SLX/wi/eAHP6jp3QRoUOJNTXwCf8YZZ6Sf/exn+U1QfFjw9NNP5+vWWGON9OMf/7imdxOgQbnvvvtyVdRxxx1Xdt2aa66ZLrroorTTTjvlDxCgoTJTCqiS0qc58Z9s/Kd6yy23pG7duuU3PNEmsummm6bp06fX9G4CNDgfffRRat26dVn41Lx58/yhwfHHH5/++Mc/ppkzZ5r9B1BgZ8Gbb76ZVlpppfzz7Nmz83URUq277rrpnXfeqeldhBollAKWyq9+9av09ttvl/382WefpRVXXDF/H5/Cjx49Ot1zzz3ppptuSldffXUN7ilA/RfDcu+4444Frovj8qhRo9J//vOfBYaeR8tIBFQrr7yyNhGA5TzUfNasWflrfAiw7bbbpieffDK99957qVmzZrnboGXLlmnVVVc17oIGTygFVFrMJYlL+/bt01tvvZWvizc3U6ZMyYHU5MmT04MPPpj/o43/gLfZZpua3mWAeh1IHXbYYWWfvMebnU8//TS/+enatWu6884782yppk3/b1pDDD2PalYAlo/4ECD+Do45fjHO4pBDDkmDBw9OO+ywQ+rQoUM666yz8ge48Xf0gAED0pw5c1Lnzp1rerehRjWar34bqIS//e1vaY899sjfX3bZZWncuHH564YbbpgOP/zwNGbMmPT444+n9dZbL917773pxhtvTHfffXfaYIMNanrXAeqdaMH74Q9/mEOpH/3oR3lOSVRBxSfwcfyNNzzxRihaRrbeeutcPRVn43vggQfSCiusYKguwHISx904Np9yyilp9dVXz2c+jUrVqJR67rnn0v33358/PIjjdRyn45hc0dmsoaEQSgFLFJ/o/PSnP81nCTnxxBNzRVR8H8PNzz777PwfbpzWNj7tif9Y4xP7CKw6duxY07sOUG+Py3Es3muvvdKBBx6Y3wBFFdTw4cNzBWvM+QvxYUGc5Slm/cVxPKqmvv7667LqKQCWvTqqceP/14B0880352DqmmuuKbsuPhiI43OcHCjOVh2te61atcq3c0ymoRNKAYtVCppGjBiRLrjggnT66afnYbkxlLFXr17p29/+di4/jkGN0SYS/7m2adMmXwBYPkqVTuecc05q165dOu200/IxOOb+RRtfLIs3RnEiivJ8Gg9QfWJuVHwocNttt5Udb+MM1BFCXXvttTlwir+No3o1PtDt379/rpxaVKAFDZF/AcAixZuXCKTiP9QQZ9S77rrr0q233ppDqHjDE29+rrzyyjxQN05nu8kmmwikAJaT0meJETp99dVX+di744475uN1nFp8yy23zHNMosV6zz33TK+88soCtxdIAVTfsTjapk8++eRcoVo63kZr3hNPPJH+/e9/5wqoCJ1inlSsuzCBFAilgMUoDSyPeSXPPvtsbtGL/vjofx8yZEgOpuJT+f/+97/pN7/5TX6DBMDyEcFThFExT6r0ZuaEE07Is/z69euXW6qjxTo+QNhnn33yso033rimdxug3omT/PzjH//I3++77765Uuqggw7KHwgccMAB+W/n6Ch4+OGH08svv5zOPffc3LbXqVOnmt51qHU0rwKL9cwzz+RPdqIEOcQZneLTnjPPPDN/+hPDde+55578ZmnFFVes6d0FqPdndIqZffEhwPbbb59bqmOO38cff5xOPfXUvO4vf/nL/IFC/BwhlnklANUrThrx+uuv53AqTvZz/vnn5+/jw4Bhw4bls1JHO9/VV1+dPyhYaaWV0u9+97t8HNdGDQvyFwqwgIXPyBRBU7zZif9440x78cYoPhF68MEH83+08Z/skUceWaP7DFDflWaSHH300bliNeZIRatenL0pZv/FwNx4M7TNNtuk//3vf+mhhx7Kx/I4pgukAKpXnDji5z//eZ4fFX8Ht2jRIg0cODCHUfGBbVROxfIjjjgiDzWPv6d9SAAV8y8CKFPRf5Rt27bNX6NEOYaal/rhY35UvCn63ve+VyP7CtDQ/PnPf0677rpr6t69e9l1M2bMSL/+9a/zGfi222679MUXX+Q3RHEs92k8wPL5ezn+Po6/iTfYYIP0ySefpKeffjrtvvvuubMggqkePXqkQYMGpR122KHsdj4kgIr5VwFkUQEV/1HG1/jU56OPPkq77bZbPnVt9MSfd955afr06Xl2Sfzne99996VHHnkkzzABYPkpnZ0pzuYUVVEhvpZOJT527Nj03e9+Nx111FFltxFIAVSv0nG1NJw8TvgTrdQx0uLee+/NodP3v//9HExFa3XMXY1WvpLynQjA/yOUAsr+k43/TGNI47e+9a0cUN1xxx357Hp9+vTJZcnRDjJq1Ki06qqrpttvv10gBbAcRLXTH//4x9wyHZ+yl94AxYcCcVyOk0tsscUW+bqoWC0/06/Ugi2QAqj+uX6vvfZauvvuu9P777+fK1dj1mrM+YsPb+MD22ipjrPwxckn4vgMLFmj+aXzWQINUrR+rLHGGvmNzPDhw/PMkgsuuCAvizPq/eEPf8if+sSskjjdbXwqH5/QV3RaWwCWTRyLY2Duo48+mo+5caamrbfeOh1++OH5w4HLL788fyJ/8cUX5yG6f/3rX/Mbod///vdpo402qundB6i31apvvvlm+slPfpLbpeNMevEBQYy2iKqo+GAgOg3iw9xYN/5+jhCrdFtg0YRS0IBF2XEMxI3AKc4cEm9y9tprr3TFFVeUrRNlx48//ng+y9Oxxx7rUx+A5Sj+LIsZUf/85z/zp+9DhgzJb4TiZBM/+MEPclt1nHL8iSeeSGuvvXaaPHlyDq/iDVK8WSo/bwqA6hFjLa677rr8YUDv3r3zddE9MHjw4FzVeu655+YxF1FBFZWsAimoPP9KoAHbZZdd0oQJE/JpbaNd74c//GF67LHHctlxSQzMjTdBcV2UJAOw/ETrXZytadKkSWn06NG5cjVCqg8//DC99NJLqWfPnumdd97JgdQtt9ySh5+PGDEi7bzzzuntt9/Ob4IAWDYzZ87MVanxddasWfmM0/E3cnxf+gBhxx13TPvvv3+uVp06dWoefh6VrRFIRVu1QAoqx78UaMDi1OFRahyf9EToFOFTlCSfdtpp6eWXXy5bLwadX3/99al169Y1ur8A9V28kYk2vXijE+3UIU43Hmd1+u1vf5vbqqNNJN4olYaev/DCC7mNLyqlvAkCWHYPPvhg/sA2LiussEI+vm655ZZp/Pjx+VIaWh4fCGy77bbf+ODWXD+oPO17QPrPf/6TLrnkkvyJT/zHGm0jzz33XL6u/KlsASjG3//+9/yBQHzyHq0gAwcOLHvTE2d7Kg02D9G6F2dFdfIJgGUTx9cpU6bklrx4mxwjLuJD3KhSjQ9wb7311tSmTZs84DzOejpgwIA8R+rOO+90dj2oIh+nAfmTnxisGxVTMVvqe9/7Xg6nYqBu/OcsuwYoVpzVac8998xDdK+66qocSJWOxeXPtBfteiuttJJACqAaRAdB375904svvphDps022yz94x//yFWqHTt2TMcff3yex3rKKaekE088MVe3xhmpY13t01A1QilggWAqZpZEldQ+++yTPw2KNz8++QEoXlRIxZySaB2pSBybtesBVJ9+/fqlVVZZJd1www357HpnnXVWPgt1zJO644478syoONte586d8wcCcWbUOEbH2akdj6Fq/MsBFgim4j/jONNTfB9tIwDUjGgbiQqpQYMG5Z99QACwfETlaVQ9tWrVKt10001p9uzZ6corr8wjLqIqKs5+GieWGD58eG7tO/nkk/Mx+Z577sljL2L2FFA1QilgAdE3/6tf/Sr3ywNQs2+QOnTokD799NOa3h2AeiuOtREwxZn1pk+fnoOp6BaI68sHUzFH6q677kpPPPFEnrn605/+NM2YMSP9/ve/z7P9gKox6BwAoJaKAboxL8qZnACqXwRPcXydMGFCPsHPhx9+mEdY9OnTJ38gEAPOY/nZZ5+duwgeeuihdMABB5S1VT///PNpvfXWS+3atavphwJ1llAKAKCOvHECoHrE2+CokHrttddy1dORRx6Z2/CiZTrap88444wcTEWV1EcffZTb+jbYYIN82zlz5ixy3h+wdDS/AgDUcgIpgOoVgdQXX3yRrrnmmnTqqaemo446Ks9VjTNR33bbbXmuVP/+/dMtt9ySrrvuulwRVSKQguojlAIAAKDBiXDpgw8+yGc7jRBqwIABOZzaf//90znnnJNnTMXZ9i644IK8vqpVqH4GnQMAAFDvRagU5s2bl0OoaMPbbbfdUvv27XOb3re+9a203377pTXXXDN17NgxtWzZMq299tpltxdIQfVTKQUAAEC9VqpyihlSgwcPzl9POumk1KtXr3z2vFjWo0ePvG4MNN99991zW1+0+UWI1bixeg5YHgw6BwAAoN57/fXX80DzuHz7299Om2++eT6rXsySius6deqUPv/88zRjxow0YsSI3N4nkILlSygFAABAva+Uuvrqq9OKK66Y+vbtW3b95MmT09tvv50rpf7617/m5XHmvQikzJCC5U/7HgAAAPVahEv/+9//UvPmzb+xrE+fPunBBx9MF154Ydl1X3/9dWra1NtlWN7UIQIAAFCvRNvdwmJ4+UcffZReeeWVsuvWXXfdtN122+UKqfIEUlAM/9IAAACoN0ptd++++256/vnn06xZs9IGG2yQDjvssPSnP/0pDRs2LA8y33XXXdOVV16ZZs6cmWdMAcUzUwoAAIB6Id7exhnzJk6cmM+mF1VQ06dPT//973/TKaeckvbaa690ww03pHHjxqV27dqlZs2apSFDhhhqDjVEpRQAAAD1QgRSH3/8cerXr1867rjjUvfu3dNXX32VRo8enU466aS02mqrpeuvvz4HVXH92muvnW9jhhTUDDEwAAAA9cZnn32WVl555fSjH/0o/xxh084775x+/vOfpxEjRuTlbdu2Teuss04OpKJCSiAFNUMoBQAAQJ218ESaL7/8MrfnjRo1Kv8cwVP41re+lVq2bJkDq/K07EHNEQcDAABQp4eaf/LJJ2nOnDn554033jgdeOCB6cEHH0yrr7562nHHHfO6//jHP1KbNm3y+kDtYNA5AAAAdXao+YQJE1Lfvn1T8+bN0+TJk/P3UREVIdTYsWNThw4d8rrTpk1L999/fx5qXrotULOEUgAAANTJCqkZM2akH//4x+mYY45Ju+22Wx5oHmfXiwHncaa9CKzGjx+fB5ofcsgheXaUoeZQewilAAAAqHPeeeed9Mgjj6TXX389XXvttWXX//nPf05nnHFGuueee9I222xTYZgF1A4mugEAAFDnjBkzJt14443p+eefT2+99VZZ6LTPPvukrbbaKr366qvfuI1ACmoXoRQAAAC12hdffJF+97vf5fa8km7duqXrr78+z4YaOXJk+uyzz8pCp7iuRYsWNbjHQGVopAUAAKDWiokzV1xxRXr00UfTyiuvnDp16pQroY444ohcFdW4ceN02WWX5SHncea9mCMVIVbXrl1reteBJVApBQAAQK22/vrrp+222y498MADqU2bNum5557LgdQll1ySz6536qmnpr/+9a95eVRIPfzww/kse3PmzKnpXQcWQygFAABArRWteFEVNWnSpNy+d8EFF6Rf//rX6ZNPPkkvvvhibuOL6z/99NM0bdq0XE0V34cIpoDaSygFAABArRXDy6P6af/99y8baH7kkUem3XbbLd13331p+PDhqWnTpmm//fZLffv2zWfk+9WvfpUDKqB2azQ/GnQBAACgFvv73/+eevXqldq2bZu22GKLNHDgwNSsWbO8bObMmblCKtxzzz35EmFV69ata3ivgcURSgEAAFAnnH766WnGjBlpyJAhqXnz5nkIerT3hdJb2/g5zsS3yiqr1PDeAkuifQ8AAIA6ISqkpk6dWuGsqFI4FVq2bFnwngFVIZQCAACgTjjhhBNyy96gQYO+EUSV/3nh64HaqWlN7wAAAAAsSbTnzZs3L3Xo0KHs7HpA3WamFAAAAHXGe++9l9Zaa63UpEmTmt4VYBkJpQAAAKhz5s6dK5iCOk4oBQAAAEDhDDoHAAAAoHBCKQAAAAAKJ5QCAAAAoHBCKQAAAAAKJ5QCAAAAoHBCKQCAesSJlQGAukIoBQBQg8aNG5fOOuus9P3vfz9tvfXWac8990znnXdeeuedd5ZqO//73//SSSedlN59991Um9x0001p0003rendAABqIaEUAEANufvuu9Phhx+ePvjgg3TGGWekoUOHpp49e6ZRo0alQw45JP33v/+t9Laee+659NRTT6Xa5sc//nH63e9+V9O7AQDUQk1regcAABqiF198MV122WXpqKOOSgMGDCi7vnPnzrla6uCDD079+/dPDz/8cKrL2rVrly8AAAtTKQUAUAN+/etfp1VWWSX17dv3G8tat26dzjnnnLTXXnulzz//PM2dOzcNGTIkHXDAAbnFb9ttt80VVv/85z/z+iNGjMgBVohAK25bcv/996f9998/bbnllrlFMNrpvv766wXu76GHHkr77bdf2mqrrdIPf/jDvN2OHTvm7Za8+eab6dRTT00777xzvv+jjz46B2slU6ZMyW16t99+e9p3333Td77znXz7hdv3lvRYAICGQygFAFADw8j/8Y9/pO9+97upefPmFa6zzz77pN69e6eWLVumgQMHpptvvjkddthh6bbbbksXX3xx+uijj1KfPn3SzJkzc9h08skn59sNGjQonXLKKfn7W2+9NZ1//vn5fgYPHpyrsqJF8IILLii7n9///vc5xNp+++3Tr371q7T33nvn20d4VDJp0qRcuRVzrmLeVexPo0aN0rHHHpteeOGFBfb7uuuuS8cff3y69NJL00477fSNx7WkxwIANBza9wAAChYhzFdffZXWWWedSq0/bdq0dPrpp+fqpJKVVlop/fznP08TJ05M2223XWrfvn2+fvPNN8/b/eyzz9Itt9ySw58IksIuu+ySVl999fzzz372s7TxxhunG264IXXp0iWHSGHXXXdNK6ywQrr22mvL7iuCrrhu+PDhuborRBAW1U7XXHNNrsYqiequQw89dJkeCwDQMAilAAAK1rjx/xWrl69GWpxSQPThhx+mt956K02ePDn97W9/y9fNmTOnwtu89NJLadasWWmPPfZYoF0vfg7PPvtsatasWXrvvfdylVJ50e5XPpSKaqgIrkqBVGjatGleL6qevvjii7LrN9lkk2p/LABA/SSUAgAoWFQrtWjRIgdCixKtbLNnz87rjhs3Ll100UX5a1QVbbTRRmnttdcuawWsyMcff5y/nnjiiYusWIpgKLRp02aBZW3btl3g508++SStscYa39hGXBf3H3Ovyl+3OFV5LABA/SSUAgCoAdFK9/zzz+c2vhVXXPEby2NIeJyd7ze/+U1ubYth4X/84x/ThhtumCutnn766fT4448vcvurrrpq2Qyn9ddf/xvLy4dHH3zwwQLLFv55tdVWSzNmzPjGNqZPn56/tmrVKodcSxLh1QknnLDUjwUAqJ8MOgcAqAHHHXdcrmaKweALi1AohoCvt956ObCK9Y455pg8A6rU+vfMM8/kr/PmzctfS9eXbLPNNnkO1NSpU/NZ9UqX0ryoOFteu3bt8iyqv/zlLwvcduGAaMcdd0wjR47Mc6pKovXwT3/6U95mtAFWxhtvvFGpxwIANAwqpQAAasC2226bZzldf/316fXXX08HHXRQrjh67bXX0rBhw/KcpiFDhqRvfetb+Qx8cfa8mOMUlwiNHnjggbydmBtVvjIqAqbddtstVyFFVVIMMo8Kpc6dO+eAKn6OM+dtttlm+eupp56azjzzzHThhRemrl27pgkTJuQ5UaEUGsVZACM4ijAp2gEjhLrrrrvy2fgiPKusDh06VOqxAAANg0opAIAacvLJJ+fgKcKhK664Igc+d955Zw6V/vCHP+Sh4TFc/Fe/+lWetxQhVr9+/fIsqgiFYi7V6NGj87YidPre976Xq6CuuuqqfN1pp52WzjnnnBxU9ejRI58pr1OnTvm2paHl3bp1SxdffHH65z//mXr27JmrnwYMGJCXrbzyyvlrVDXdc889ueXv3HPPTWeddVbenzgbX9xnZVX2sQAADUOj+SZKAgA0WDHbqWPHjmmDDTYou+6pp55KJ510Ug7GoqIKAGB5EEoBADRgUZ0V7YNRVRWtgm+++Wa68cYb8zyrqNoCAFhehFIAAA3YRx99lFv+YmbUhx9+mFv09t577zxrKlrqAACWF6EUAAAAAIUz6BwAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAwgmlAAAAACicUAoAAACAVLT/D5eqeCxAAPatAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1200x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from matplotlib.ticker import FuncFormatter\n",
    "faturamento_ordenado = faturamento_categoria.sort_values(ascending = False)\n",
    "fig, ax = plt.subplots(figsize = (12,7))\n",
    "def formatador_milhares(y, pos):\n",
    "    return f'R$ {y/1000:,.0f}K'\n",
    "formatter = FuncFormatter(formatador_milhares)\n",
    "ax.yaxis.set_major_formatter(formatter)\n",
    "faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette(\"viridis\", len(faturamento_ordenado)))\n",
    "ax.set_title('Faturamento por Categoria', fontsize = 16)\n",
    "ax.set_xlabel('Categoria', fontsize = 12)\n",
    "ax.set_ylabel('Faturamento', fontsize = 12)\n",
    "plt.xticks(rotation = 45, ha = 'right')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1f206ae-dd89-439c-8b7e-e3d82256e911",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42388e4e-cdd8-4849-b894-45a28977d3e2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9c76b1c-77ef-47c9-a539-d38105797e1b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78f1ccc6-736f-45d7-9f3c-d4faffe6b407",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "870e3b2e-5329-4f56-ac96-e4da17938236",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43d8d9db-b8d6-47f9-b4f1-a9180d8220c6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0adb4e0-e004-4bff-a1ac-6c6839cbabae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "781a0055-6bf2-49c1-8503-3bdda196b667",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "428ffe0d-d005-48ce-beef-31689b0e74be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f22238ad-61a3-4ae6-85f8-55f84bd8e451",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d524f2a-41ff-4f4a-85ad-f911f46cf18f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f951854-2387-4525-a625-110a5d52efa1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "910a965d-fbd4-48b7-874b-58632828599d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ec92227-1fd4-4d72-b2b5-4d24e8c300ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12b6da10-a324-42a0-a2cb-d9e01e6e90bd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60d56fd3-350a-4f8b-bdf4-c5b0ab45fbe9",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
