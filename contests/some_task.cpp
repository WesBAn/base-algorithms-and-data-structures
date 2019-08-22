#include <iostream>
int main() {
    int n, x;
    int prev;
    std::cin >> n;
    if (n > 0) {
        std::cin >> prev;
        std::cout << prev << std::endl;
        for (int i = 1; i < n; ++i) {
            std::cin >> x;
            if (x != prev) {
                std::cout << x << std::endl;
                prev = x;
            }
        }
    }
    return 0;
}
