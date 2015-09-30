# Bonus problem -- from Google tech talk at Olin 9/29/15

# Two Androids parachuted out of an airplane and landed on a one-dimensional
# line. They dropped their parachutes when they landed. Write a routine for
# both Androids to run so they find each other.

# Each Android can use the following functions:
# -> move_left -- take one step to the left in 1 unit of time
# -> move_right -- take one step to the right in 1 unit of time
# -> wait -- delay in place for 1 unit of time
# -> on_parachute -- the Android is standing on a parachute
# -> androids_met -- the Androids are in the same place

def test_bench(android1_loc, android2_loc):
  world = World(android1_loc, android2_loc)
  android1 = Android(android1_loc, world)
  android2 = Android(android2_loc, world)

  while not androids_met(android1, android2):
    android1.routine()
    android2.routine()

  numSteps = len(android1.track)
  meetingLoc = android1.loc

  print "Androids met at location %s after %s steps" % (meetingLoc, numSteps)


def androids_met(android1, android2):
  return android1.loc == android2.loc


class World:
  def __init__(self, parachute1_loc, parachute2_loc):
    self.parachute_locs = [parachute1_loc, parachute2_loc]

  def is_parachute(self, loc):
    return loc in self.parachute_locs


class Android:
  def __init__(self, loc, world):
    self.parachute_loc = loc
    self.loc = loc
    self.world = world
    self.moving_right = True
    self.amplitude = 1 # increasing oscillation until parachute located
    self.track = [loc]

  def move_left(self):
    self.loc = self.loc - 1
    self.track.append(self.loc)

  def move_right(self):
    self.loc = self.loc + 1
    self.track.append(self.loc)

  def wait(self):
    self.track.append(self.loc)
    return

  def on_parachute(self):
    return self.world.is_parachute(self.loc)

  def routine(self):
    if self.on_parachute() and self.loc != self.parachute_loc:
      # Wait at the other android's parachute if you find it
      self.wait()
    elif self.moving_right:
      if self.loc < self.parachute_loc + self.amplitude:
        self.move_right()
      else:
        # Turn around (going left now) after reaching amplitude
        self.moving_right = False
        self.move_left()
    else:
      if self.loc > self.parachute_loc:
        self.move_left()
      else:
        # Turn around (going right now) after reaching own parachute
        # & increase amplitude
        self.moving_right = True
        self.amplitude = self.amplitude + 1
        self.move_right()
