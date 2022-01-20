# Cosmos Role

```shell
COSMOS_CHAIN_NAME=osmosis molecule -v converge -s cosmos
```
## Requirements

Golang to be installed


## References

* [Cosmos-SDK based chains registry](https://github.com/cosmos/chain-registry/)




chain_bin_flags: "--x-crisis-skip-assert-invariants" starts syncing the node since the last upgrade until it is at the current height.



Its from the SDK's pruning modes. Basically how much of history you want to be able to query. If you don't care about querying blocks older than now, you can use pruned. if you want to query only a couple historical heights prior to download height, and certain 'threshold blocks' (Every 500th IIRC?) you can use default pruning.

This doesn't matter for after the sync height. So if you just want to join the network, and query latest state, you can download a pruned node, and then run a default pruning setup afterwards.

https://github.com/cosmos/cosmos-sdk/blob/master/store/types/pruning.go

	// PruneDefault defines a pruning strategy where the last 362880 heights are
	// kept in addition to every 100th and where to-be pruned heights are pruned
	// at every 10th height. The last 362880 heights are kept assuming the typical
	// block time is 5s and typical unbonding period is 21 days. If these values
	// do not match the applications' requirements, use the "custom" option.
	PruneDefault = NewPruningOptions(362880, 100, 10)

	// PruneEverything defines a pruning strategy where all committed heights are
	// deleted, storing only the current height and where to-be pruned heights are
	// pruned at every 10th height.
	PruneEverything = NewPruningOptions(0, 0, 10)

	// PruneNothing defines a pruning strategy where all heights are kept on disk.
	PruneNothing = NewPruningOptions(0, 1, 0)

# default: the last 100 states are kept in addition to every 500th state; pruning at 10 block intervals
# nothing: all historic states will be saved, nothing will be deleted (i.e. archiving node)
# everything: all saved states will be deleted, storing only the current state; pruning at 10 block intervals
# custom: allow pruning options to be manually specified through 'pruning-keep-recent', 'pruning-keep-every', and 'pruning-interval'
pruning = "default"

# These are applied if and only if the pruning strategy is custom.
pruning-keep-recent = "0"
pruning-keep-every = "0"
pruning-interval = "0"