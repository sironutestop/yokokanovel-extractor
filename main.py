# -*- coding:utf-8 -*-
import io
import re
from typing import List, Tuple, Union

# 横岡小説を判定させるためのテキスト
SEARCH_TEXT = r"横岡は"
# 横岡小説の抽出対象となるテキスト
TALK_HISTORY_PATH = "line-history-text/talk_history.txt"
# 一つ当たりのメッセージの塊を判別する、テキストセパレート用の正規表現
SEPARATE_PATTERN = r"\d{2}:\d{2}\s+"


class TextExtractionForMultipleLine:
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
        file_path (str):
        separate_pattern (str):
        search_word_pattern (str):
        extraction_separate_text (bool): 抽出する文字列に、separate_pattern の箇所も含めるか。
                                            True: 含める False: 含めない
                                            (上記 Example の箇所だと、「hh:mm」が該当する)

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

    def _initialization(self, file: io.TextIOWrapper) -> str:
        """文字列をサーチするファイルの初期化を行う。
        Args:
            file (io.TextIOWrapper): オープンしたテキストファイル。
        Returns:
            str: 探索を開始する先頭行の文字列を返します。
        """
        for line in file:
            if re.match(self._separate_pattern, line):
                return line

        print("初期化処理に失敗しました")
        raise ValueError("separate_pattern に合致する行が見つかりませんでした")

    def _search_word(self, file: io.TextIOWrapper, search_head_text: str) -> List[str]:
        """文字列にサーチする文字列が含まれるか確認する。
        Args:
            file (io.TextIOWrapper): オープンしたテキストファイル。
            search_head_text (str): 一回で確認する行の先頭の文字列。
        Returns:
        """
        extract_text_list = []

        # 探索するテキストをひとまとめにする
        search_group_text = search_head_text
        for line in file:

            # 次の行がセパレートする行のやつ、もしくはファイルの最終行だった場合(line == "")はテキストグループのチェックをする
            if re.match(self._separate_pattern, line) or line == "":
                # ひとまとめにしたテキストから、検索するワードが含まれるか確認する
                for search_group_line in search_group_text:
                    if re.search(self._search_word_pattern, search_group_line):
                        extract_text_list.append(search_group_text)

                # 次回検索の先頭行のテキストで、探索するテキストを上書きする。
                search_group_text = line

            else:
                search_group_text = search_head_text + line

        return extract_text_list

    def extraction(self) -> Union[List[str], None]:
        """抽出処理を実行する。
        Args:
        Returns:
        """
        extract_text_list = []

        with open(self._file_path, encoding="utf-8") as f:
            search_head_text = self._initialization(f)
            extract_text_list = self._search_word(f, search_head_text)

        return extract_text_list

    def print_extraction_text(self) -> None:
        """抽出したテキストのリストを標準出力へ出力する。
        Args:
        """
        print("処理実行")


def main() -> None:
    # テスト用
    test = TextExtractionForMultipleLine(TALK_HISTORY_PATH, SEPARATE_PATTERN, SEARCH_TEXT)
    print(test.extraction())


if __name__ == "__main__":
    main()
