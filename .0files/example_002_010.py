import ray

pages = [
    """One of the unique parts of Ray is its emphasis on actors. Actors give you tools to manage the execution state, 
    which is one of the more challenging parts of scaling systems. Actors send and receive messages, updating their 
    state in response. These messages can come from other actors, programs, or your main execution thread with the Ray 
    client. For every actor, Ray starts a dedicated process. Each actor has a mailbox of messages waiting to be 
    processed. When you call an actor, Ray adds a message to the corresponding mailbox, which allows Ray to serialize 
    message processing, thus avoiding expensive distributed locks. Actors can return values in response to messages, so 
    when you send a message to an actor, Ray immediately returns a future so you can fetch the value when the actor is 
    done processing your message.""",

    """Actors have a long history before Ray and were introduced in 1973. The actor 
    model is an excellent solution to concurrency with state and can replace complicated locking structures. Some other 
    notable implementations of actors are Akka in Scala and Erlang."""
]

pages = ray.data.from_items(items=pages)

print(pages.take(0))

if __name__ == '__main__':
    print(type(pages))
    words = pages.map(lambda x: x['item'].split(' '))  # .map(lambda w: (w, 1))  # .groupby(lambda wc: wc['item'][0])
    # print(words.take(0))
    # print(type(words))
    # grouped_words = words.groupby(lambda wc: wc[0])
    # print(words)
