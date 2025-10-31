from hierarchical import HierachicalClustering
import numpy as np

class AgglomerativeClustering(HierachicalClustering):
    def fit(self, data):
        clusters = [
            {
                'id': i,
                'points': [i]
            } for i in range(len(data))
        ]

        distance_matrix = np.zeros( (len(data), len(data)) )
        next_cluster_index = len(data)

        history = []
        
        for i in range(len(data)):
            for j in range(len(data)):
                distance = self.distance_strategy.calculate(data[i], data[j])
                distance_matrix[i, j] = distance
                distance_matrix[j, i] = distance

        print(f'Distance Matrix:\n{distance_matrix}\n')

        while len(clusters) > 1:
            min_distance = float('inf')
            cluster_to_merge = (None, None)

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    dist = self.linkage_strategy.calculate(clusters[i]['points'], clusters[j]['points'], distance_matrix)

                    if dist < min_distance:
                        min_distance = dist
                        cluster_to_merge = (i, j)

            i, j = cluster_to_merge
            cluster_i_id = clusters[i]['id']
            cluster_j_id = clusters[j]['id']

            new_cluster = {
                'id': next_cluster_index,
                'points': clusters[i]['points'] + clusters[j]['points']
            }

            clusters[i] = new_cluster
            clusters.pop(j)

            history.append( [cluster_i_id, cluster_j_id, min_distance, len(new_cluster['points'])] )

            next_cluster_index += 1

        return history

            # print(f'Posição i: {cluster_i_id} - Posição j: {cluster_j_id} - {min_distance}')
            # print(f'Cluster: {new_cluster['id']}: {new_cluster['points']} - Qtd {len(new_cluster['points'])}')

            # print(f'Estado atual: { [cluster['points'] for cluster in clusters] }')

        # while len(clusters) > 1:
        #     min_distance = float('inf')
        #     cluster_a_index = -1
        #     cluster_b_index = -1

        #     for i in range(len(clusters)):
        #         for j in range(i + 1, len(clusters)):
        #             dist = distance_matrix[clusters[i]['id'], clusters[j]['id']]
        #             if dist < min_distance:
        #                 min_distance = dist
        #                 cluster_a_index = i
        #                 cluster_b_index = j

        #     cluster_a = clusters[cluster_a_index]
        #     cluster_b = clusters[cluster_b_index]

        #     new_cluster = {
        #         'id': next_cluster_index,
        #         'points': cluster_a['points'] + cluster_b['points']
        #     }
        #     next_cluster_index += 1

        #     clusters.append(new_cluster)

        #     for i in range(len(clusters) - 1):
        #         if i != cluster_a_index and i != cluster_b_index:
        #             dist_a = distance_matrix[cluster_a['id'], clusters[i]['id']]
        #             dist_b = distance_matrix[cluster_b['id'], clusters[i]['id']]
        #             new_distance = self.linkage_strategy.calculate(dist_a, dist_b)
        #             distance_matrix[new_cluster['id'], clusters[i]['id']] = new_distance
        #             distance_matrix[clusters[i]['id'], new_cluster['id']] = new_distance

        #     clusters.pop(max(cluster_a_index, cluster_b_index))
        #     clusters.pop(min(cluster_a_index, cluster_b_index))
