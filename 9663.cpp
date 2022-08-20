#include <iostream>
#include <vector>
#include <utility>
#include <time.h>

void makeTable(int num, std::vector<std::pair<int, int>>& chessTable);
bool checkEnablePlace(const std::pair<int, int> queenLoacation, const std::vector<std::pair<int, int>>& chessTable);

int result = 0;

int main() {
	/* 빠른 입출력 */
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	int num;
	std::vector<std::pair<int, int>> chessTable;
	std::cin >> num;

	clock_t start = clock();
	makeTable(num, chessTable);
	std::cout << result << "\n";
	clock_t end = clock();

	std::cout << "Running time: " << (end - start) / CLOCKS_PER_SEC << "\n";

	return 0;
}

void makeTable(int num, std::vector<std::pair<int, int>>& chessTable) {
	if (num == chessTable.size()) {
		result++;
		return;
	}

	//for (int row = chessTable.size() + 1; row <= num; row++) {
		for (int col = 1; col <= num; col++) {
			if (checkEnablePlace(std::make_pair(chessTable.size(), col), chessTable) == true) {
				chessTable.push_back(std::make_pair(chessTable.size(), col));
				makeTable(num, chessTable);
				chessTable.pop_back();
			}
		}
	//}
	return;
}

bool checkEnablePlace(const std::pair<int, int> queenLoacation, const std::vector<std::pair<int, int>>& chessTable)
{
	for (std::pair<int, int> eachQueen : chessTable) {
		if ((queenLoacation.first == eachQueen.first || queenLoacation.second == eachQueen.second) //같은 행, 열에 있는 경우
			|| (queenLoacation.first + queenLoacation.second == eachQueen.first + eachQueen.second) || //(/)형태의 대각선인 경우
			(queenLoacation.first - eachQueen.first == queenLoacation.second - eachQueen.second)) //(\)형태의 대각선인 경우
			return false;
	}
	return true;
}