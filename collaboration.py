class CollaborativePlanner:
    def __init__(self):
        self._shared_itineraries = {}
        self._collaborators = {}
    
    def share_itinerary(self, itinerary_id, owner, collaborators):
        self._shared_itineraries[itinerary_id] = {
            "owner": owner,
            "collaborators": collaborators
        }
        for collaborator in collaborators:
            if collaborator not in self._collaborators:
                self._collaborators[collaborator] = []
            self._collaborators[collaborator].append(itinerary_id)
    
    def get_shared_itineraries(self, user):
        return self._collaborators.get(user, [])
    
    def add_collaborator_comment(self, itinerary_id, user, comment):
        if itinerary_id in self._shared_itineraries:
            if "comments" not in self._shared_itineraries[itinerary_id]:
                self._shared_itineraries[itinerary_id]["comments"] = []
            self._shared_itineraries[itinerary_id]["comments"].append({
                "user": user,
                "comment": comment
            })
            return True
        return False
