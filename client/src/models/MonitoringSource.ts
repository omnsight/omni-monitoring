/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SourceType } from './SourceType';
export type MonitoringSource = {
    /**
     * Name of the monitoring source
     */
    name?: (string | null);
    /**
     * Describe what kind of information the source focuses on
     */
    description?: (string | null);
    /**
     * Type of the monitoring source such as 'website', 'twitter', 'telegram'
     */
    type?: (SourceType | null);
    /**
     * URL of the monitoring source
     */
    url?: (string | null);
    /**
     * Reliability score of the monitoring source, ranging from 0 to 100
     */
    reliability?: (number | null);
    /**
     * The last time the source was reviewed, in epoch time
     */
    last_reviewed?: (number | null);
    /**
     * Platform-specific identifiers or handles required to monitor the source via API calls. Examples include a Twitter user id or a Telegram channel ID.
     */
    attributes?: (Record<string, any> | null);
    /**
     * ArangoDB document ID
     */
    _id?: (string | null);
    /**
     * ArangoDB document key
     */
    _key?: (string | null);
    /**
     * ArangoDB document revision
     */
    _rev?: (string | null);
    /**
     * Data creation timestamp
     */
    created_at?: (number | null);
    /**
     * Data update timestamp
     */
    updated_at?: (number | null);
    /**
     * Identify the user the monitoring source belongs to
     */
    owner: string;
};

