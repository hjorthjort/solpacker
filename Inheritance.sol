pragma solidity ^0.8.0;

contract A {
    uint128 a;
}
contract B {
    uint256 b;
}

contract C is B, A {
    uint128 c;
}