{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "random practice",
      "provenance": [],
      "authorship_tag": "ABX9TyOYsL11ylnwbkpbakHTCeas",
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
        "<a href=\"https://colab.research.google.com/github/manu727/streamlitpractice/blob/main/random_practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YZnaAdcAuh_b",
        "outputId": "f80fe833-fee0-458a-e147-7e1a2daec18e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the current hour: 12\n",
            "Enter the number of hours to add: 6\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "currentHour = int(input(\"Enter the current hour: \"))\n",
        "hoursToAdd = int(input(\"Enter the number of hours to add: \"))\n",
        "remainder = hoursToAdd%24\n",
        "finalTime=currentHour+remainder\n",
        "if finalTime>12:\n",
        "    x=(12-currentHour)\n",
        "    k=remainder-x\n",
        "    print(k)\n",
        "else:\n",
        "    print(finalTime)"
      ]
    }
  ]
}