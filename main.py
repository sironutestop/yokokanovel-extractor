# -*- coding:utf-8 -*-
import re
from typing import List, Union

# 横岡小説を判定させるためのテキスト
SEARCH_TEXT = "横岡は"
TALK_HISTORY_PATH = "line-history-text/talk_history.txt"


class SearchMultipleText:
    """複数行テキストファイルから、特定の文字列が含まれる内容を抽出するクラス

    複数行テキストを特定の規則に従って抽出し、それを必要に応じて
    特定の文字列が含まれているものを抽出する。

    Example:
        以下の <テキストファイル> から、hh:mm から始まり、次に hh:mm から始まる行までの
        行をひとまとまりのテキストで扱い
        サーチする文言を「クラス」とすると、<結果> の内容が取得できる。

        <テキストファイル>
            hh:mm id1 テスト内容1行目
            テスト内容2行目
            吾輩はクラスである。
            hh:mm id2 テスト内容3行目
            テスト内容4行目
            吾輩はメソッドである。

        <結果>
            hh:mm id1 テスト内容1行目
            テスト内容2行目
            吾輩はクラスである。


    Attributes:
        text_path (str):
        separate_pattern (str):
        search_word (str):
        extraction_separate_text (bool): 抽出する文字列に、separate_pattern の箇所も含めるか。
                                            True: 含める False: 含めない
                                            (上記 Example の箇所だと、「hh:mm」が該当する)

        extract_text (list:str): 抽出したテキストのリスト

    """

    def __init__(
        self,
        file_path: str = "",
        separate_pattern: str = "",
        search_word_pattern: str = "",
        is_extract_separate_text: bool = False,
    ) -> None:
        if (file_path == "") or (separate_pattern == "") or (search_word_pattern == ""):
            raise ValueError("引数の値はすべて指定してください")

        self._file_path = file_path
        self._separate_pattern = separate_pattern
        self._search_word_pattern = search_word_pattern
        self._is_extract_separate_text = is_extract_separate_text
        self._extract_text = ""

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        if file_path == "":
            raise ValueError("値が指定されていません")
        self._file_path = file_path

    @property
    def separate_pattern(self) -> str:
        return self._separate_pattern

    @separate_pattern.setter
    def separate_pattern(self, separate_pattern: str) -> None:
        if separate_pattern == "":
            raise ValueError("値が指定されていません")
        self._separate_pattern = separate_pattern

    @property
    def search_word_pattern(self) -> str:
        return self._search_word_pattern

    @search_word_pattern.setter
    def search_word_pattern(self, search_word_pattern: str) -> None:
        if search_word_pattern == "":
            raise ValueError("値が指定されていません")
        self._search_word_pattern = search_word_pattern

    @property
    def is_extract_separate_text(self) -> bool:
        return self._is_extract_separate_text

    @is_extract_separate_text.setter
    def is_extract_separate_text(self, is_extract_separate_text: bool) -> None:
        if is_extract_separate_text == "":
            raise ValueError("値が指定されていません")
        self._is_extract_separate_text = is_extract_separate_text

    def print_setting_values(self) -> None:
        """標準出力へ設定を出力する。
        Args:
        """
        # 環境によって改行コードなどに差分があることを考慮し、
        # 設定用変数ごとに print で出力
        print("file_path: " + self._file_path)
        print("separate_pattern: " + self._separate_pattern)
        print("search_word_pattern: " + self._search_word_pattern)
        print("extraction_separate_text: " + str(self._is_extract_separate_text))

    def _initialization(self):
        """文字列をサーチするファイルの初期化を行う。
        Args:
        Returns:
        """
        print("初期化実行")

    def _check_search_text(self):
        """1回でサーチする文字列を抽出する。
        Args:
        Returns:
        """
        print("サーチ用文字列の抽出実行")

    def _search_word(self):
        """文字列にサーチする文字列が含まれるか確認する。
        Args:
        Returns:
        """
        print("文字列にサーチする文字列が含まれるかチェックし、抽出実行")

    def extraction(self) -> Union[List[str], None]:
        """抽出処理を実行する。
        Args:
        Returns:
        """

        self._initialization()
        self._check_search_text()
        self._search_word()

    def print_extraction_text(self) -> None:
        """抽出したテキストのリストを標準出力へ出力する。
        Args:
        """
        print("処理実行")


def main() -> None:
    # テスト用
    test = SearchMultipleText(TALK_HISTORY_PATH, "", SEARCH_TEXT)
    test.print_setting_values()


if __name__ == "__main__":
    main()
