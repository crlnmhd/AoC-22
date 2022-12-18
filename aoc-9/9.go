package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

type direction int

const (
	Upp direction = iota
	Down
	Left
	Right
)

type head_move struct {
	towards direction
	steps   int
}

type position struct {
	x int
	y int
}

func main() {
	head_moves, err := getHeadMoves()
	if err != nil {
		return
	}
	//fmt.Println("Part1:", part1(head_moves))
	fmt.Println("Part2:", part2(head_moves))
}

var tailPositionMoveGvenRelativeHead = map[position]position{
	// top
	{x: -1, y: -2}: {x: -1, y: -1},
	{x: 0, y: -2}:  {x: 0, y: -1},
	{x: 1, y: -2}:  {x: 1, y: -1},
	// right side
	{x: 2, y: -1}: {x: 1, y: -1},
	{x: 2, y: 0}:  {x: 1, y: 0},
	{x: 2, y: 1}:  {x: 1, y: 1},
	// bottom
	{x: -1, y: 2}: {x: -1, y: 1},
	{x: 0, y: 2}:  {x: 0, y: 1},
	{x: 1, y: 2}:  {x: 1, y: 1},
	// left side
	{x: -2, y: -1}: {x: -1, y: -1},
	{x: -2, y: 0}:  {x: -1, y: 0},
	{x: -2, y: 1}:  {x: -1, y: 1},
}

func part1(head_moves []head_move) int {
	tailPosition := position{x: 0, y: 0}
	headPosition := position{x: 0, y: 0}
	visits := make(map[position]uint)

	for _, move := range head_moves {
		fmt.Println("move: ", move)
		for i := 0; i < move.steps; i++ {
			headPosition = getNewHeadPosition(&headPosition, move.towards)
			fmt.Println("head:", headPosition)
			tailPosition, _ = getNewTailPosition(&tailPosition, &headPosition)
			visits[tailPosition] += 1 // Technically no need to do more than mark the postion.
			fmt.Println("Visiting: ", tailPosition)
		}
	}
	return len(visits)
}

func part2(head_moves []head_move) int {
	var knotPositions [10]position
	tailVisits := make(map[position]uint)
	showKnots(&knotPositions)
	for _, move := range head_moves {
		for i := 0; i < move.steps; i++ {
			knotPositions[0] = getNewHeadPosition(&knotPositions[0], move.towards)
			for knotIndex := 1; knotIndex < len(knotPositions); knotIndex++ {
				headPostion := knotPositions[knotIndex-1]
				tailPosition := knotPositions[knotIndex]
				fmt.Println("Moving tail: ", tailPosition, "after  head: ", headPostion)
				tailPosition, err := getNewTailPosition(&tailPosition, &headPostion)
				if err != nil {
					fmt.Println("ERROR. Rope is broken!\n\n ")
					showKnots(&knotPositions)
					os.Exit(2)
				}
				knotPositions[knotIndex] = tailPosition
			}
			tailVisits[knotPositions[len(knotPositions)-1]] += 1
		}
	}
	return len(tailVisits)
}

func showKnots(knots *[10]position) {
	const offset int = 30
	startingPos := position{x: knots[0].x - offset, y: knots[0].y - offset}
	for row := startingPos.y; row < startingPos.y+(2*offset); row++ {
		for col := startingPos.x; col < startingPos.x+(2*offset); col++ {
			currentPosition := position{x: col, y: row}
			var symbol string = "."
			for knotIndex := len(knots) - 1; knotIndex >= 0; knotIndex-- {
				if knots[knotIndex] == currentPosition {
					symbol = strconv.Itoa(knotIndex)
				}
			}
			fmt.Print(symbol)
		}
		fmt.Println()
	}
}

func getNewTailPosition(tail *position, head *position) (position, error) {
	positionRelateiveToHead := position{
		x: head.x - tail.x,
		y: head.y - tail.y,
	}

	fmt.Println("Head:", head, "tail:", tail, "Relative: ", positionRelateiveToHead)
	if intAbs(positionRelateiveToHead.x)+intAbs(positionRelateiveToHead.y) > 4 {
		fmt.Println("Something is wrong! Too large relative step.")
		return position{0, 0}, errors.New("Error moving head after tail")

	} else if intAbs(positionRelateiveToHead.x) == intAbs(positionRelateiveToHead.y) &&
		intAbs(positionRelateiveToHead.x) == 2 {
		return position{
			x: tail.x + positionRelateiveToHead.x/2,
			y: tail.y + positionRelateiveToHead.y/2,
		}, nil
	}

	tailMove := tailPositionMoveGvenRelativeHead[positionRelateiveToHead] // Defaults to {0, 0}
	fmt.Println("tail move:", tailMove)
	return position{
		x: tail.x + tailMove.x,
		y: tail.y + tailMove.y,
	}, nil
}

func getNewHeadPosition(head *position, moveDirection direction) position {
	newHeadPosition := *head
	if moveDirection == Upp {
		newHeadPosition.y -= 1
	} else if moveDirection == Down {
		newHeadPosition.y += 1
	} else if moveDirection == Right {
		newHeadPosition.x += 1
	} else if moveDirection == Left {
		newHeadPosition.x -= 1
	}
	return newHeadPosition
}

func getHeadMoves() ([]head_move, error) {
	const fileName = "input.txt"
	file, err := os.Open(fileName)

	if err != nil {
		fmt.Println("Error opening file")
		return nil, err
	}
	defer file.Close()

	var head_moves []head_move

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		var direction string
		var steps int

		_, err = fmt.Sscanf(line, "%s %d", &direction, &steps)
		if err != nil {
			fmt.Printf("Error parsing: %s\n", line)
			return nil, err
		}
		head_moves = append(head_moves, head_move{towards: parseDirectionString(direction), steps: steps})
	}
	return head_moves, nil
}

func intAbs(x int) int { // math.Abs is float64 only.
	if x < 0 {
		return -x
	} else {
		return x
	}
}

func parseDirectionString(str string) direction {
	if str == "D" {
		return Down
	} else if str == "U" {
		return Upp
	} else if str == "L" {
		return Left
	} else {
		return Right // FIXME error handling...
	}
}
